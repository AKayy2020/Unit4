# p4_lib.py
from passlib.context import CryptContext

# code for database handler
import sqlite3


class DatabaseWorker:
    def __init__(self, name):
        self.connection = sqlite3.connect(name)
        self.cursor = self.connection.cursor()

    def search(self, query):
        result = self.cursor.execute(query).fetchall()
        return result

    def get(self, query):
        result = self.cursor.execute(query).fetchone()
        return result

    def run_save(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def close(self):
        self.connection.close()


# password encryption
# Create an object of the class CryptContext
pwd_config = CryptContext(schemes=["pbkdf2_sha256"],
                          default="pbkdf2_sha256",
                          pbkdf2_sha256__default_rounds=30000)


# this function receives the unsafe password
# and return the hashed password
def encrypt_password(user_password):
    return pwd_config.encrypt(user_password)


def check_password(hashed_password, user_password):
    return pwd_config.verify(user_password, hashed_password)
