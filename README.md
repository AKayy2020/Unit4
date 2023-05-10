# Project 4: Konbinet, the best social media
![Hotpot (1)](https://user-images.githubusercontent.com/89135778/230832513-d6722d51-e9ed-41e6-be9a-35451d10d151.png)

# Criteria A: Planning
## Problem definition
My client is the co-owner of a little resource-limited convenience store at a local school. After meeting with her _(see Appendix A)_, I learned that every Thursday she opens her "Konbini", where she sells products to students and some teachers. 

However, she feels like it is hard to know which products the customers want the most, their opinion about them, and how to promote customer-to-customer interaction. She has tried to send emails with feedback forms but students seem to ignore them because they are not attractive and practical.
She also does not know how to reach more people and to get more customers, and how to improve Konbini's marketing. As students are very busy, she thinks they would not have time for in-person events. 
Right now, if a sudden happens and she cannot open the store one day or there are new products selling, she does not have any effective communication method to tell customers. She usually puts physical posters around school, but this is little convenient and time-consuming. Something to take into consideration is that many students are underage in the country she lives in, but client does not know how to keep the privacy and data of students safe. 

It is also hard for her to keep track of the exact numbers of how many customers she has, how interactive are they with the store, and which is the price range of her products. She tried to keep a Google Spreadsheet with numbers of how many customers she had, but she gave up quickly as it was very complex. The time she manages is also little, as the end of the school year is soon.

## Rationale for the proposed solution
According to the client's needs, I will develop a Social Networking Service (SNS) in the form of a website. The website will have an initial landing page where potential users will be called to sign up and log in, with a system with encrypted passwords to increase security. Once the user has passed the login system, a main menu will appear. There, users will be able to write posts and interactuate with other users by writing posts, uploading images, and sending private messages. Additionally, managers will be able to add news and products with their prices. The client needs Python, HTML, CSS, and SQLite, as they are suitable tools for this kind of project. 

HTML is a good option because all websites are written in it, making it widely used for web development [^1]. It provides a semantic and structured way to organize web content, which improves website accessibility and search engine optimization.[^2] This means that my client will be able to have a traditional website, which is her objective.

Following that, 97.2% of websites also use some degree of CSS [^3]. CSS is the best tool to complement HTML: it gives easy customization of website design, making it visually appealing and user-friendly [^4]. It also separates content, which facilitates website maintenance and updating.[^5] The combination of HTML and CSS can provide a clean and lightweight website. All this will help my client into what she wants as a website.

For developing this project, I could have also used Javascript and Bootstrap as a complement to HTML, as they are powerful tools for website development.[^6] However, using them would have increased the complexity of the project and they would have slowed down its development, not meeting the client’s expectations related to time. Additionally, HTML and CSS allow the development of a clean and lightweight website that loads quickly and efficiently, so they are overall the best solution.

Python is a good choice because its codes can be easily written and executed much faster than other programming languages[^7]. Python is an open source with many libraries to complement the code[^8], so there are multiple options for personalization for fulfilling the client's necessities. Python is also good for the client, as it is free and my client will not need to buy a license[^9].

For data management, I will need to create a database to control the data of the users: their login information, the posts they write, and the private messages they send. For doing so, SQLite is a great tool. It is an easy and simple way to look at and get all the data. SQLite is lightweight, efficient, and easy to integrate into Python programs [^10]. It does not require a separate server process or system, and data can be stored in a single file, making it easy to manage [^11]. Other tools for data management are N1QL. However, this one is difficult to use without the help of Couchbase, a multi-model database software. It can also have bad speed and bad synchronization support for web-based programs [^12], something that can affect the reputation of my client’s konbini store.

Overall, the combination of Python, HTML, CSS, and SQLite provides a cost-effective, efficient, and user-friendly solution to the client's needs for an SNS Konbini website.


[^1]: “Choosing the Best Programming Language for Web Development”, Turing https://www.turing.com/kb/best-web-development-language-for-project .
[^2]: “HTML: A good basis for accessibility”, MDN Mozilla https://developer.mozilla.org/en-US/docs/Learn/Accessibility/HTML .
[^3]:”Usage Statistics of CSS for Websites”, W3 Techs,May 2023. https://w3techs.com/technologies/details/ce-css .
[^4]: “What Is CSS and Why Should You Use It?”, DevMountain https://devmountain.com/blog/what-is-css-and-why-use-it/ .
[^5]: “Benefits of CSS in Search Engine Optimization”, Search Engine Journal, 2006 https://www.searchenginejournal.com/benefits-of-css-in-search-engine-optimization/4149/ .
[^6]: “What are some alternatives to CSS 3?”, StackShare, https://stackshare.io/css-3/alternatives
[^7]: “Advantages of Python over Other Programming Languages.” Vilmate, 2019, https://vilmate.com/blog/python-vs-other-programming-languages/ .
[^8]: “About Python.” Python.org, https://www.python.org/about/. 
[^9]: “About Python.” Python.org, https://www.python.org/about/. 
[^10]: “Appropriate Uses For SQLite”, https://www.sqlite.org/whentouse.html .
[^11]: “Distinctive Features Of SQLite”, SQLite https://www.sqlite.org/different.html
[^12]: “10 Best Microsoft SQL Alternatives for Data Querying”, Turing, https://www.turing.com/kb/10-sql-alternatives .


## Success criteria:
After meeting with the client _(See Appendix B)_, we agreed on the following success criteria for the website:
1. The website has a landing page showing its features and calling users to register.
2. The rest of the pages are hidden under a secure registration and login system with requirements for passwords and email.
3. There is an updates section that can be edited only by the managers.
4. The website shows the products available and their price, which only managers can edit.
5. The website allows users to write posts and upload pictures that other users can see.
6. There is a one-to-one private message system where users can communicate with each other.
7. The website gives statistical information: numbers about users, posts, and products.


# Criteria B: Design

## Record of Tasks
| Task No | Planned Action                           | Planned Outcome                                                                                                  | Time estimate | Target completion date | Criterion |
|---------|------------------------------------------|------------------------------------------------------------------------------------------------------------------|---------------|------------------------|-----------|
| 1       | First meeting with client                | Client described her requiremetns for the project                                                                | 10min         | Apr 3                  | A         |
| 2       | Write Problem Scenario                   | Explain problem given by client in previous meeting                                                              | 10min         | Apr 6                  | A         |
| 3       | Research tools that will be used         | Find proposed solution for client's problem                                                                      | 10min         | Apr 7                  | A         |
| 4       | Write Rationale of the Proposed Solution | Have a better understanding of project's goal according to client's needs                                        | 15min         | Apr 10                 | A         |
| 5       | Write Success Criteria                   | Success criteria that meets client's needs                                                                       | 15min         | Apr 10                 | A         |
| 6       | Second meeting with client               | Approval of Proposed Solution and Success Criteria                                                               | 10min         | Apr 11                 | A         |
| 7       | Draw System Diagram                      | Create a visual representation of the system architecture.                                                       | 20min         | Apr 11                 | B         |
| 8       | Draw Wireframe Diagram                   | Create a visual representation of the user interface.                                                            | 1h            | Apr 12                 | B         |
| 9       | Draw ER diagram                          | Create a visual representation of the data model.                                                                | 15min         | Apr 12                 | B         |
| 10      | Draw Flowchart #1 for algorithms         | Create a visual representation of the algorithm for XXX.                                                         | 20min         | Apr 13                 | B         |
| 11      | Draw Flowchart #2 for algorithms         | Create a visual representation of the algorithm for XXX.                                                         | 30min         | Apr 13                 | B         |
| 12      | Draw Flowchart #3 for algorithms         | Create a visual representation of the algorithm for yet another specific function.                               | 45min         | Apr 13                 | B         |
| 13      | Third meeting with client                | Obtain approval from the client on the design overview proposal.                                                 | 10min         | Apr 14                 | B         |
| 14      | Write Test Plan                          | Create a detailed plan for testing the system to ensure it meets the success criteria.                           | 10min         | Apr 14                 | B         |
| 15      | Code Python base                         | The code in which my program will be based, functions such as create_database, populate_db, and project library. | 1h            | Apr 16                 | C         |
| 16      | Code landing page                        | A landing page with basic information about the project.                                                         | 30min         | Apr 18                 | C         |
| 17      | Code sign-up page                        | A sign-up page with validation for input fields.                                                                 | 1h            | Apr 19                 | C         |
| 18      | Code login page                          | An integrated login system with the sign-up system.                                                              | 1h            | Apr 20                 | C         |
| 19      | Code home page                           | A home page with a navigation bar integrated with the login system.                                              | 45min         | Apr 20                 | C         |
| 20      | Code forum page base                     | Forum page base that will be later integrated with other pages.                                                  | 10min         | Apr 21                 | C         |
| 21      | Code forum page post system              | Forum page with a form that saves posts in the database and displays them.                                       | 1h            | Apr 21                 | C         |
| 22      | Code landing page CSS                    | A user-friendly landing page                                                                                     | 10min         | Apr 22                 | C         |
| 23      | Code login and sign-up CSS               | A user-friendly login system                                                                                     | 10min         | Apr 23                 | C         |
| 24      | Code home page CSS                       | A user-friendly home page                                                                                        | 10min         | Apr 23                 | C         |
| 25      | Code forum page CSS                      | A user-friendly forum page                                                                                       | 15min         | Apr 23                 | C         |
| 26      | Code account page base                   | Account page with basic data of the user: email, username, date joined                                           | 30min         | Apr 22                 | C         |
| 27      | Integrate forum and account pages        | Account page can display posts made by the user on the forum page                                                | 30min         | Apr 22                 | C         |
| 28      | Code images page HTML                    | A web page to display images.                                                                                    | 1h            | Apr 23                 | C         |
| 29      | Code images page Python                  | The Python code to implement the images page.                                                                    | 1h            | Apr 23                 | C         |
| 30      | Code images database                     | The database to store the images.                                                                                | 10min         | Apr 24                 | C         |
| 31      | Integrate images system code             | Integrate the images system code into the website                                                                | 30min         | Apr 24                 | C         |
| 32      | Code updates page HTML                   | A web page to display updates.                                                                                   | 10min         | Apr 24                 | C         |
| 33      | Code updates page Python                 | The Python code to implement the updates page.                                                                   | 20min         | Apr 25                 | C         |
| 34      | Integrate updates sections               | A functional updates section                                                                                     | 15min         | Apr 28                 | C         |
| 35      | Code updates CSS                         | A user-friendly updates page                                                                                     | 20min         | Apr 28                 | C         |
| 36      | Code messages system Python              | A page that allows one to one comunication, with a form, an Inbox and an Outbox                                  | 1h            | Apr 28                 | C         |
| 37      | Code messages system HTML                | A page that allows one to one comunication, displayed in the website.                                            | 1h            | Apr 28                 | C         |
| 38      | Integrate message system                 | A functional private messages section                                                                            | 45min         | Apr 29                 | C         |
| 39      | Code messages section CSS                | A user-friendly private messages page                                                                            | 20min         | Apr 29                 | C         |
| 40      | Code admin requirements                  | Functions as posting updates and deleting posts will only be accessible for admin                                | 1h            | Apr 29                 | C         |
| 41      | Code login requirements                  | Login requirements for accessing most pages of website                                                           | 30min         | Apr 30                 | C         |
| 42      | Write tools used for unit 3              | Tools used section in documentation                                                                              | 30min         | Apr 30                 | C         |
| 43      | Code statistics page                     | A statistics section that shows information about website, in home                                               | 30min         | Apr 30                 | C         |
| 44      | Integrate statistics page                | A functional statistics page                                                                                     | 30min         | May 1                  | C         |
| 45      | Improve overall CSS                      | A user-friendly website, with clearly organized CSS                                                              | 20min         | May 1                  | C         |
| 46      | Use the final website as a user          | Test functionality of the website and ensure that it runs without errors                                         | 30min         | May 1                  | D         |
| 47      | Write video script                       | Develop a clear and logical script that covers all important points of the project                               | 1h            | May 2                  | D         |
| 48      | Record video                             | Video demonstrating the functionality of the project                                                             | 15min         | May 3                  | D         |
| 49      | Edit video                               | Ensure the privacy of the client and developer in the video                                                      | 45min         | May 3                  | D         |
| 50      | Add code files to product folder         | Files in the product folder to allow future extensibility                                                        | 20min         | May 4                  | D         |
| 51      | Write feedback questionnaire             | Questionnaire to gather feedback from beta testers and the client                                                | 30min         | May 4                  | E         |
| 52      | Beta tester tries website                | Have a beta tester evaluate the website and provide feedback                                                     | 1h            | May 5                  | E         |
| 53      | Client tries website                     | Have the client test the website and provide feedback                                                            | 1h            | May 5                  | E         |
| 54      | Discuss with client                      | Feedback by the client and address any concerns or issues                                                        | 45min         | May 6                  | E         |
| 55      | Analyze client feedback                  | Identify areas for improvement                                                                                   | 1h            | May 6                  | E         |
| 56      | Write about client's meeting             | Document the feedback and discussions from the meeting with the client                                           | 30min         | May 7                  | E         |
| 57      | Write first recommendation               | A recommendation for improving the functionality of the website                                                  | 10min         | May 9                  | E         |
| 58      | Write second recommendation              | A second recommendation for improving the functionality of the website                                           | 10min         | May 9                  | E         |
| 59      | Write third recommendation               | A third recommendation for improving the functionality of the website                                            | 10min         | May 9                  | E         |

**Table 2:** Record of Task- showing the planning and working process of the project. All the steps are related to Planning, Solution Overview analysis and Development, and Functionality (criterias A, B C, and D). The target completion date and the time estimate for each task is also shown.


## Internal structure plan (design)
I will design and make a SNS website for promoting business-customer relations for a client who is a convenience store manager at a local school. The program will consist on an website for being able to write posts and comments about the Konbini's products, plus being able to read news and updates about it and some statistical information. It is constructed using the softwares Python, HTML, CSS, and SQLite. It will take 3 weeks to make and will be evaluated according to the criteria A, B, C, D, and E.

### System Diagram
**Figure 1:**

![project_unit4](https://github.com/PaulaYaniz/Unit4/assets/89135778/5b2c417a-01a0-4d1a-9421-0ae7f3b251d8)

Fig.1 is the System Diagram. It shows the brand and type of the computer, with its specifications and the Operative System is has. The program runs in Python 3.8 and uses different languages: Python, HTML, CSS, SQLite.

### Wireframe Diagram
**Figure 2:**

![project4-wireframe drawio](https://github.com/PaulaYaniz/Unit4/assets/89135778/4e1ce61a-8b53-4e1c-9055-8d9e2835f32b)

Fig.2 is the Wirefram Diagram for the program.

### Entity Relationship (ER) Diagram
**Figure 3:**

![project4-erd drawio](https://github.com/PaulaYaniz/Unit4/assets/89135778/2b4ec19d-93d4-40ed-aac2-8a987a4f255e)

**Figure 4:**

![project4-databases drawio](https://github.com/PaulaYaniz/Unit4/assets/89135778/35f5a367-951e-49a2-b8e7-82af95ef7d9a)

Fig. 3 is the ER diagram for the database that my program uses.

Fig. 4 is a screenshot of the tables in the database of my program.

### UML Diagrams
**Figure 4:**

![project4-uml drawio](https://github.com/PaulaYaniz/Unit4/assets/89135778/2e5db87f-42fd-4cba-8690-612b0f13420b)

Fig. 4 is the UML diagram for the class of my program.

### Flow Diagrams
![project4-flowch-login drawio](https://github.com/PaulaYaniz/Unit4/assets/89135778/c206b8b5-5f28-4a13-8a70-1ab7a20ca3f5)

**Figure 5**

Fig. 5 is the flow diagram for my login system.

## Test Plan
| SC | TEST                                                           | DESCRIPTION                                                                                                         | PROCEDURE                                                                                                                                                                        | EXPECTED OUTPUT                                                                                                                                                     |
|----|----------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1  | Unit testing for landing page (functional)                     | Evaluation of landing page characteristics and buttons                                                              | 1. User enters the web address 2. User clicks sign up button 3. User clicks login button                                                                                         | User appears in landing page as first result. Buttons are functional and lead user to new pages for registration.                                                   |
| 2  | Unit testing of sign up page (functional)                      | This test evaluates the sign up page validation system                                                              | 1. User clicks sign up button,  2. In form, user does not follow password and email requirements: password="PASSSS" and email="232424M"                                          | An error message will be shown, explaining why it is incorrect. For example, "password should have an uppercase, a lowercase, a number, and a special character".   |
| 2  | Unit testing of sign up/login system (functional, integration) | This test evaluates the whole sign up and login system                                                              | 1. User enters "stuart", "stuart@gmail.com", "Stuart12!" in sign up form. 2. User enters same values in login form.                                                              | User successfully logged in with "stuart" username.                                                                                                                 |
| 2  | Unit testing for login required pages (functional)             | This test evaluates if the pages needed are under login requirements and innaccesible for registered users          | 1. User not logged in adds "/home", "/forum", "/messages", "/account", "/updates", "/images" to web address                                                                      | User is unable to visualize those pages and is redirected to the login page.                                                                                        |
| 3  | Unit testing of writing new update (functional)                | This test is evaluating how the admin adds a new update into the updates database and deletes it.                   | 1. Click updates navigation button. 2. Complete the form with "Title of Update" and "Content of Update". 3. Delete the published update just made by clicking the delete button. | Admin will appear in Updates Section. Update written in form is added in database and displayed below. Update deleted is deleted from database and from display.    |
| 3  | Unit testing of writing new update (functional)                | This test is evaluating how the user tries to add a new update into the updates database and delete it.             | 1. Click updates navigation button. 2. Complete the form with "Title of Update" and "Content of Update". 3. Delete published update by clicking the delete button.               | User will appear in Updates Section. There is no updates form if user is a basic user. There are no delete buttons in the updates for basic users.                  |
| 4  | Unit testing of adding new product and price (functional)      | This test is evaluating how the admin adds a new product and its price into the products database and deletes it.   | 1. Click home navigation button. 2. Complete the form with "Pocari Sweat" and "145". 3. Delete the published product just made by clicking the delete button.                    | Admin will appear in Home Section. New product written in form is added in database and displayed below. Product deleted is deleted from database and from display. |
| 4  | Unit testing of adding new product and price (functional)      | This test is evaluating how user tries to add a new product and its price into the products database and delete it. | 1. Click home navigation button. 2. Complete the form with "Pocari Sweat" and "145". 3. Delete a product by clicking the delete button.                                          | User will appear in Home Section. There is no product form if user is a basic user. There are no delete buttons in the products for basic users.                    |
| 5  | Unit testing of writing new post (functional)                  | This test is evaluating how the user adds a new post into the posts database.                                       | 1. Click Forum navigation button. 2. Complete the form with "It is crazy" and "It is crazy how Konbini is so cheap"                                                              | The post will be saved in the database and automatically displayed with datetime and username of user logged in                                                     |
| 5  | Unit testing for uploading an image (functional)               | This test is evaluating how user uploads pictures and displaus tem                                                  | 1. Click Images navigation button 2. Paste the image link in the form, for example "https://pocarisweatme.com/wp-content/uploads/2022/02/Frame-4.jpg"                            | Image will be added to to uploaded images folder and database. Image will be automatically displayed.                                                               |
| 6  | Unit testing for sending 1-1 messages (functional)             | This test is evaluating how user is able to send messages to another user                                           | 1. Log in as stuart. 2. Click Messages navigation button. 3. Complete form with "I love you kevin" and "but I love Konbinet more" to username "kevin"                            | Sent message will appear in Outbox section                                                                                                                          |
| 6  | Unit testing for receiving 1-1 messages (functional)           | This test is evaluating how user is able to receive messages from another user                                      | 1. Log in as kevin. 2. Click Messages navigation button.                                                                                                                         | Received message from "stuart" will appear in Inbox section                                                                                                         |
| 7  | Unit testing for statistics (functional)                       | Statistics appear in a text message in the user's screen.                                                           | 1. Click the Statistics navigation button 2. Add new post in Forum Section, values="Check stats" and "this is just a test" 3. Click the Statistics navigation button again       | Statistics will appear and they will change when users enter new data in the posts section.                                                                         |
| -  | Quality of code review (non-functional)                        | Use of comments, tabs, and developer-friendly files and variable names                                              | Check if the program is developer-friendly                                                                                                                                       | Program will have comments on every step of the code, and variable names are easy to understand.                                                                    |
| -  | File organisation review (non-functional)                      | Are all files organised? Folders, files, etc                                                                        | Check Pycharm folder and delete files that have not been used for the project.                                                                                                   | On the project folder all files should have user-friendly names. All files are organised inside the folder.                                                         |

**Table 1:** Test plan- showing the test plan for my website. The description, expected output, and procedure for each test is also shown.

# Criteria C: Development

## Explanation of Techniques and Evidence
- Functions
- For/while loops
- Input Validation
- Conditional statements
- Encryption
- Relational databases
- Variables
- Lists
- Error handlers
- Base templates extensions
- Tags
- Content block
- Use of files and/or databases to save/load persistent data: SQLite database to store user information, posts, products, updates, images, and messages.
- Use of dynamic data structures: dictionaries to store user data in session cookies.
- Use of multiple programming languages: Python, HTML, Jinja2 templates, CSS.
- Use of object-oriented design: encapsulate database access and password encryption and checking functionality in a separate module (p4_lib.py).
- Use of nested control structures: password validation in the signup function.


## Code
* More details on the comments of the code

### Sign up page
![image](https://github.com/PaulaYaniz/Unit4/assets/89135778/ca2db793-c1b7-4c68-9d06-2519769904e5)

```.py
# password requirements
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

# sign up system
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

```
```.html
{% extends "p4_base_landing.html" %}
{% block content %}
<main>
    <h1>Sign Up</h1>
    <h3 class="error">{{ error_msg }}</h3>
    <form action="/signup" method="post">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required><br><br>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br><br>

        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required><br><br>

        <input type="submit" value="Sign Up" class="submit-btn">
    </form>

    <p>You are already registered? <a href="/login">Log in</a>.</p>
</main>
{% endblock %}
```
According to the client’s needs, more specifically Success Criteria 2, I developed a sign up system.

This code includes a Flask route for a sign-up page that allows users to create an account in my website. After clicking on the Sign Up button, user goes to ‘/signup’ URL, where they can complete a form with their email, username, and password.

For this code, I have used my Computational Thinking Skills. I have used Decomposition, the process of breaking down a complex problem into more manageable parts, for the whole sign up system: checking password requirements, checking if an account already exists, inserting new user’s data in the database, etc.

I use Algorithmic thinking skills in the ‘password_requirements’ function. This function checks if the length of the password is at least 8, then uses pattern recognition to check if there is at least one uppercase, one lowercase, one number, and one special character in the password created by the user. Finally, it uses abstraction to return a boolean value according to if the requirements are met or not.. 

I use the Flask framework to handle HTTP requests and responses. The function ‘signup()’ handles GET and POST requests that come from ‘/signup’. If the request is GET, then the function renders the signup page, that is an HTML template. If the request is POST, the function processes the form data submitted by user.

I use a dictionary for the ‘request.form’, where I get data from the form in the page using the POST request. The email, username, and password are extracted from the form and stored in separate variables.

When I use the ‘password_requirements’ function it checks if password meets certain requirements. If it doesn't meet the requirements, an error message is displayed, which is saved in a variable (initially blank). If not, function checks if the email or username already exists in the database. If they exist, another error message is displayed. If they don't exist, the function inserts the new user's data into the database, with the hashed password (I use a function for hashing it).

If the function encounters any errors, it renders the sign up page again, displaying the appropriate error message. The error message is passed to the HTML template as a parameter called ‘error_msg’.

If the user does not exist in the database, the function inserts the user's data into the database, creating the new user, it gets the user_id. The function also sets cookies with the user's ID and redirects the user to the home page.

During the development process, a problem I encountered was how to store user data and how to retrieve it later to check if a user exists or not, correctly. My solution was to use an SQLite database and a DatabaseWorker class to insert and get data in the database. I use SQLite databases to create tables, insert data, and search for data using the SQL queries. Another problem was how to securely store user passwords in the database. My solution was to use a secure password encryption algorithm and store the encrypted password in the database.

For HTML, my code consists of the use of a template for all the common code parts of the website, following with the DRY (Don’t Repeat Yourself) programming principle. After that I have a h1 tag (as a title), an space for the error message in case there is one, and the form with the fields the user has to choose.

### Login requirements for page visualization 
```.py
    # login is required for this action
    if 'user' not in session:
        return redirect(url_for('login'))
```
According to Success Criteria 1, my user needs that key pages in the website are available only to users logged in. That is why I have this code, which I use in the pages with this requirement.

Following with the previous code provided, where I show how I create 'user', this first line checks with a conditional statement if the ‘user’ key is present in the session, which is where user data is stored after logging in. If ‘user’ is not present in the session, it means that the user has not logged in, so the boolean of False would return, not allowing user to visualize the page, and redirecting them to  the login page.


For this I have use the KISS (Keep It Simple, Stupid!) programming principle, as it is a basic code but very useful.

I learned how to do this by accessing https://pythonbasics.org/flask-sessions/ .

### One-to-one messages system
![image](https://github.com/PaulaYaniz/Unit4/assets/89135778/50ca2426-5d9c-456e-b68f-cf848d5722fb)
```.py
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
```
```.html
{% extends "p4_base_logged.html" %}
{% block content %}
<main class="forum">
    <div class="forum-grid">
        <div class="new-post">
            <h2>New Message</h2>
            <form class="post-form" method="POST">
                <label for="message-receiver">To:</label>
                <input type="text" id="message-receiver" name="message-receiver" required>
                <label for="message-title">Title:</label>
                <input type="text" id="message-title" name="message-title" required>
                <label for="message-content">Content:</label>
                <textarea id="message-content" name="message-content" rows="8" required></textarea>
                <button type="submit" class="submit-btn">Submit</button>
            </form>
        </div>
        <div class="forum-posts">
            <h2>Inbox</h2>
            {% for message in messages_in %}
            <div class="post">
                <h3 class="post-title">{{ message[3] }}</h3>
                <p class="post-content">{{ message[4] }}</p>
                <div class="post-meta">
                    <span>Received from {{ message[1] }} on {{ message[5] }}</span>
                </div>
            </div>
            {% endfor %}
        </div>
         <div class="forum-posts">
            <h2>Outbox</h2>
            {% for message in messages_out %}
            <div class="post">
                <h3 class="post-title">{{ message[3] }}</h3>
                <p class="post-content">{{ message[4] }}</p>
                <div class="post-meta">
                    <span>Sent to {{ message[2] }} on {{ message[5] }}</span>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>
</main>
{% endblock %}
```
According to Success Criteria 6, my client needs a one-to-one messaging system.

For doing so, I have used Algorithmic thinking: in conditional statements, loops, and SQL queries to handle user input and interact with databases. For example, Abstraction (encapsulating the database interactions in a separate class DatabaseWorker). Decomposition (breaking down the task into smaller functions, like getting messages from database, inserting new messages into database, and rendering HTML templates).

If the user is logged in and a program receives a POST request (user submitting a message), the function gets the message details from the HTML form and inserts them into the messages table in the database using an SQL query. If GET request (nothing needs to be clicked, it is automatic), the function gets all messages received or sent by the user from the database using two SQL queries and renders the p4_messages.html template, passing in the messages as parameters.

That was one problem I had during the development process: I had to figure out how to distinguish between the messages that the users receive and the messages they send. The solution was to use an SQL query to filter the data according to which messages had the name of my user as a value in different columns (WHERE receiver='{username}' ORDER BY id DESC, for example). If it was in the receiver column, I would add that to a list called ‘messages_in’, and if my user was the sender to ‘messages_out’. This technique was an adequate solution because it is a standard way of filtering data with SQL queries into a relational database and is efficient in terms of time and memory complexity. Then I would use those lists to display the messages with HTML, doing a loop instead of hard-coding to avoid breaking DRY and KISS principles.

The website that helped me in the SQL queries was: https://blog.hubspot.com/marketing/sql-tutorial-introduction

## Ingenuity
Some of the good coding practices I have followed are:
- Descriptive variable names
- Form input validation: Sign up form, for example.
- Exceptions/error handling
- Use of autocomplete attributes in username and email to improve user experience
- Use of whitespaces and indentations for developer’s readability
- Code organization: folders, tags (headers, footers, body, main, etc)
- Comments when needed
- Use of camelCase for classes, snake_case for functions and variables, kebab-case for CSS attributes.
- Use of DRY (Don’t Repeat Yourself) programming principle for my HTML pages: I only had two template bases that I used in all the rest of the pages. Also for saving my queries for the database.

Example of error handling:
```.py
# error handling
@app.errorhandler(Exception)
def handle_error(e):
    return "Oops, there's an error. Please notify the admin in admin@gmail.com and go back", 500
```
![image](https://github.com/PaulaYaniz/Unit4/assets/89135778/cd02489a-d820-4cc2-9ee2-dd5aa7e23913)

# Criteria D: Functionality & Extensibility

## Functionality
google drive link

## Extensibility
Program files are available in the project folder.

# Criteria E: Evaluation
## Evaluation
After meeting with the client _(see Appendix X for full interview transcript)_, I got to the conclusion that I successfully satisfied the client’s needs and goals for this website.

### Beta tester evaluation:
After meeting with my beta tester (see Appendix X for interview transcript), I discovered that as a loyal Konbini client, Mr. D. is happy with the website and says he will start using it to connect with other Konbini fans about his favorite products. He likes the statistical information and the prices tables, which he finds interesting and useful. However, he did not like that the posts do not have a like button, and agreed with the developer that it should be added (see Recommendations section for more details).

### Client evaluation:
The product satisfied all the success criteria initially established.
1. The first thing I see when entering the link is a welcome page (landing page). I like that it contains pictures of what the website does once registered. I felt excited about registering!
2. I liked how the website had the privacy needed: all the important parts of the website are behind the registration page. I can also see how there are password requirements to increase security. However, it should not let students from outside the school to register, so it should only allow users with the school’s email domain.
3. I see how I can quickly write an update for my clients to see, and delete it when needed. This is solving many problems for me!
4. I also like how I can update very fast the prices and products available at the store. I am satisfied with that!
5. I am fascinated by how effectively users can write posts, and I love even more than I am able (as an admin) to delete them. This will allow me to delete all the posts that criticize my store, thank you!
6. I found the statistics part very interesting, I wondered for a long time which where the numerical data and info of the users and products.

## Recommendations
1. Add a likes function for the posts. Currently, users can just publish the posts, but cannot interact with them. A good extension would be to allow users to indicate which posts are their favorite, as many social media do. I think this would be manageable, but would require modifying the data that each post contains in the database to include those likes.

2. Allow users to write comments on other users’ posts. By allowing the creation of a chain of comments related to the same post, interaction will increase too, and ideally a sense of community too. I think this is possible but hard to do, as it would require making new requests and creating new forms, or even maybe another page dedicated to this.



# APPENDIX
### Appendix A
DEVELOPER: Good morning! Thank you for meeting with me today. You contacted me as a developer, what do you need help with?

CLIENT: I run a little convenience store at a local school and I have trouble knowing what products my customers want the most, and how to promote interaction between them. I am looking for a way to improve communication with customers and get feedback on the products I sell.

DEVELOPER: I see. Could you give me more information? What are your problems?

CLIENT: I feel like it is hard to know which products the customers want the most, their opinion about them, and how to promote customer-to-customer interaction. I also do not know how to reach more people and to get more customers, and how to improve Konbini's marketing. As students are very busy, I think they would not have time for in-person events. Also many students are underage in the country she lives in, and I do not know how to keep the privacy and data of students safe. 

DEVELOPER: I see. So, you're looking for a way to reach out to your customers more effectively, and to get their feedback on your products. What other options have you tried before? Did they work?

CLIENT: I tried but I don't know where to start. I don't have time and I am lost most of the time in everything related to the marketing and promotion of customer interaction. I tried to send emails with feedback forms but students seem to ignore them because they are not attractive and practical. Oh! Also, right now, if a sudden happens and I cannot open the store one day or there are new products selling, I do not have any effective communication method to tell customers. I usually put physical posters around school, but this is little convenient and time-consuming. I also tried to keep a Google Spreadsheet with numbers of how many customers she had, but I gave up quickly as it was very complex. 

DEVELOPER: Understood, what about the time?

CLIENT: End of the school year is soon, so I would need my website quite fast, let’s say 3 weeks.

DEVELOPER: I will see what I can do for you. Let’s have a second meeting soon so I can present you the rationale for the proposed solution and the success criteria.

### Appendix B
DEVELOPER: Hello beloved customer! It is great to see you again. 

CLIENT: Hello! Do you have the rationale for the proposed solution as we agreed last meeting?

DEVELOPER: Yes! [Rationale for the proposed solution shown]

CLIENT: It is amazing! You did a great job in identifying my needs. It looks as if you knew me personally! What about the success criteria?

DEVELOPER: Thank you! This is the success criteria [success criteria shown]. What do you think?

CLIENT: That sounds perfect! I agree with everything.

DEVELOPER: Thank you! Let's get started with your SNS website.
