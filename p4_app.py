import sqlite3
from datetime import datetime
import os
import re
from flask import Flask, render_template, request, redirect, url_for, make_response, session
from werkzeug.utils import secure_filename

from p4_lib import DatabaseWorker, encrypt_password, check_password
import requests

app = Flask(__name__)
app.secret_key = os.urandom(24)

app.config['UPLOAD_FOLDER'] = os.path.join('static', 'uploaded_images')

def create_database():
    db = DatabaseWorker("p4_database.db")
    query_user = """CREATE table if not exists users (
        id INTEGER PRIMARY KEY,
        email TEXT,
        username TEXT,
        password TEXT,
        joined DATETIME DEFAULT CURRENT_TIMESTAMP
    )"""
    query_post = """CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY,
    title TEXT,
    content TEXT,
    username TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )"""
    # on delete cascade means that when a user is deleted all their posts get deleted too

    query_products = """CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    price INTEGER
    )"""
    query_updates = """CREATE TABLE IF NOT EXISTS updates (
    id INTEGER PRIMARY KEY,
    title TEXT,
    content TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )"""
    query_images = """CREATE TABLE IF NOT EXISTS images (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    file_url TEXT NOT NULL
    )"""
    query_messages = """CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY,
    sender TEXT,
    receiver TEXT,
    title TEXT,
    content TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )"""

    all_queries = [query_user, query_post, query_products, query_updates, query_images, query_messages]
    for query in all_queries:
        db.run_save(query)
    db.close()


def populate_db():
    users = []
    db = DatabaseWorker("p4_database.db")
    for user in users:
        email, username, password = user
        query = f"""INSERT into users(email, username, password) values
        ('{email}','{username}','{encrypt_password(password)}')"""
        db.run_save(query)
    db.close()


def password_requirements(password):
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[1-9]', password):
        return False
    return True


# landing page
@app.route('/')
def landing_page():
    db = DatabaseWorker("p4_database.db")
    num_users = db.search(f"SELECT COUNT(*) from users")[0][0]
    num_posts = db.search(f"SELECT COUNT(*) from posts")[0][0]
    avg_posts = round(float(num_posts / num_users), 2)
    num_products = db.search(f"SELECT COUNT(*) from products")[0][0]
    avg_price = round(db.search(f"SELECT AVG(price) from products")[0][0], 2)
    db.close()
    return render_template("p4_landingpage.html", num_users=num_users, num_posts=num_posts, num_products=num_products, avg_price=avg_price, avg_posts=avg_posts)


# sign up page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    # error message is initially blank
    message = ""
    # when user clicks "SUBMIT" button in form
    if request.method == 'POST':
        # get user data from sign up form
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']

        # password requirements not being followed
        if not password_requirements(password):
            message = "Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one number, and one special character."
        else:
            # check if account already exists
            db = DatabaseWorker("p4_database.db")
            user = db.search(f"SELECT * from users where email = '{email}' or username = '{username}'")
            # if user is in database, exists
            if user:
                message = "Username or email already exists. Try log in."
            else:
                # put data from form into database
                query = f"""INSERT into users(email, username, password, joined) values ('{email}', '{username}','{encrypt_password(password)}','{datetime.now()}')"""
                db.run_save(query)
                # get user id
                user = db.search(f"SELECT * from users where email = '{email}'")[0]
                user_id = user[0]
                # get values for saving in cookies
                session['user'] = {
                    'id': user_id,
                    'username': username,
                    'email': email,
                    'joined': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                }
                # redirect to home, logged in, with cookies
                response = make_response(redirect(url_for('home')))
                response.set_cookie('user_id', f"{user_id}")
                db.close()
                return response
    return render_template("p4_signup.html", error_msg=message)


# login
@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ""
    # get form data inputted by user
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = DatabaseWorker("p4_database.db")
        user = db.search(f"SELECT * from users where username = '{username}'")
        if user:
            user = user[0]  # because search function requires a list
            id, email_db, username, hashed, joined = user
            if check_password(hashed_password=hashed, user_password=password):
                session['user'] = {'email': email_db, 'username': username, 'password': hashed}
                response = make_response(redirect(url_for('home')))
                response.set_cookie('user_id', str(id))
                return response
        else:
            message = "Incorrect username or password"
    return render_template("p4_login.html", error_msg=message)


# log out
@app.route('/', methods=['GET', 'POST'])
def logout():
    if request.method == 'POST' or request.method == 'POST':
        # Clear the session and redirect to the login page
        session.clear()
        return redirect(url_for('login'))
    else:
        response = make_response(render_template('p4_landingpage.html'))
        response.set_cookie("user_id", "", expires=0)
        return response


# home
@app.route('/home', methods=['GET', 'POST'])
def home():
    # login is required for this action
    if 'user' not in session:
        return redirect(url_for('login'))
    # update products
    if request.method == 'POST':
        # get product written from form
        name = request.form['product-name']
        price = request.form['product-price']
        # insert new update in database
        db = DatabaseWorker("p4_database.db")
        query = f"""INSERT INTO products (name, price) VALUES ('{name}', '{price}')"""
        db.run_save(query)
        db.close()
    # delete products
    if request.method == 'GET':
        # get product written from form
        idd = request.args.get('product-id')
        # delete in database
        db = DatabaseWorker("p4_database.db")
        query = f"""DELETE FROM products WHERE id='{idd}'"""
        db.run_save(query)
        db.close()

    # get all products
    db = DatabaseWorker("p4_database.db")
    products = db.search("SELECT * from products ORDER BY id DESC")
    db.close()
    return render_template("p4_home.html", products=products)


# forum
@app.route('/forum', methods=['GET', 'POST'])
def forum():
    # login is required for this action
    if 'user' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        # get post written from form
        title = request.form['post-title']
        content = request.form['post-content']
        username = session['user']['username']
        # insert new post in database
        db = DatabaseWorker("p4_database.db")
        query = f"""INSERT INTO posts (title, content, username) VALUES ('{title}', '{content}', '{username}')"""
        db.run_save(query)

    # delete posts
    if request.method == 'GET':
        # get post written from form
        idd = request.args.get('post-id')
        # delete in database
        db = DatabaseWorker("p4_database.db")
        query = f"""DELETE FROM posts WHERE id='{idd}'"""
        db.run_save(query)
        db.close()

    # get all posts from database to display later
    db = DatabaseWorker("p4_database.db")
    posts = db.search("SELECT * FROM posts ORDER BY id DESC")
    db.close()
    return render_template('p4_forum.html', posts=posts)


# account
@app.route('/account')
def account():
    # login required for this action
    user_id = request.cookies.get('user_id')
    if not user_id:
        return redirect(url_for('login'))
    # get user logged in from database
    db = DatabaseWorker("p4_database.db")
    user = db.search(f"SELECT * from users where id = '{user_id}'")
    if user:
        user = user[0]
        id, email, username, hashed, joined = user
        # Convert joined to datetime for putting on website
        joined = datetime.strptime(joined, '%Y-%m-%d %H:%M:%S')
        user_data = {
            'id': id,
            'email': email,
            'username': username,
            'joined': joined.strftime('%Y-%m-%d %H:%M:%S')
        }
        # get all posts made by user from database
        db = DatabaseWorker("p4_database.db")
        session_user = session['user']['username']
        posts = db.search(f"SELECT * FROM posts WHERE username='{session_user}' ORDER BY id DESC")
        db.close()
        return render_template('p4_account.html', user_data=user_data, posts=posts)
    else:
        return redirect(url_for('login'))


# updates
@app.route('/updates', methods=['GET', 'POST'])
def updates():
    # login is required for this action
    if 'user' not in session:
        return redirect(url_for('login'))
    # update news
    if request.method == 'POST':
        # get post written from form
        title = request.form['update-title']
        content = request.form['update-content']
        # insert new update in database
        db = DatabaseWorker("p4_database.db")
        query = f"""INSERT INTO updates (title, content) VALUES ('{title}', '{content}')"""
        db.run_save(query)

    # delete updates
    if request.method == 'GET':
        # get update written from form
        idd = request.args.get('update-id')
        # delete in database
        db = DatabaseWorker("p4_database.db")
        query = f"""DELETE FROM updates WHERE id='{idd}'"""
        db.run_save(query)
        db.close()

    # get all updates from database to display later
    db = DatabaseWorker("p4_database.db")
    updates = db.search("SELECT * FROM updates ORDER BY id DESC")
    db.close()
    return render_template('p4_updates.html', updates=updates)


# images
@app.route('/images', methods=['GET', 'POST'])
def images():
    # login is required for this action
    if 'user' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST' and 'image-url' in request.form:
        # Save the image to the server
        url = request.form['image-url']
        response = requests.get(url)
        if response.status_code == 200:
            file_url = secure_filename(url.rsplit('/', 1)[-1])
            with open(os.path.join(app.config['UPLOAD_FOLDER'], file_url), 'wb') as f:
                f.write(response.content)

            username = session['user']['username']
            # Save the file_url to the database
            conn = sqlite3.connect('p4_database.db')
            c = conn.cursor()
            c.execute("INSERT INTO images (username, file_url) VALUES (?, ?)", (username, file_url))
            conn.commit()
            conn.close()

    # get the files from the database and pass them to the template
    conn = sqlite3.connect('p4_database.db')
    c = conn.cursor()
    c.execute("SELECT file_url FROM images")
    files_url = [os.path.join(app.config['UPLOAD_FOLDER'], row[0]) for row in c.fetchall()]
    conn.close()

    return render_template('p4_images.html', image_urls=files_url)

# messages
@app.route('/messages', methods=['GET', 'POST'])
def messages():
    # login is required for this action
    if 'user' not in session:
        return redirect(url_for('login'))

    # when user clicks submit in the form
    if request.method == 'POST':
        # get message written from form
        sender = session['user']['username']
        receiver = request.form['message-receiver']
        title = request.form['message-title']
        content = request.form['message-content']
        # insert new message in database
        db = DatabaseWorker("p4_database.db")
        query = f"""INSERT INTO messages (sender, receiver, title, content) VALUES ('{sender}', '{receiver}', '{title}', '{content}')"""
        db.run_save(query)
        db.close()

    # get all posts from database to display later
    db = DatabaseWorker("p4_database.db")
    # get username of user logged in
    username = session['user']['username']
    # lists for messages sent or received by user logged in
    messages_in = db.search(f"""SELECT * FROM messages WHERE receiver='{username}' ORDER BY id DESC""")
    messages_out = db.search(f"""SELECT * FROM messages WHERE sender='{username}' ORDER BY id DESC""")
    db.close()
    return render_template('p4_messages.html', messages_in=messages_in, messages_out=messages_out)


# error handling
@app.errorhandler(Exception)
def handle_error(e):
    return "Oops, there's an error. Please notify the admin in admin@gmail.com and go back", 500

create_database()
populate_db()

if __name__ == '__main__':
    app.run()
app.run(debug=True)
