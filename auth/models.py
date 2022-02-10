from app import db
from sqlalchemy import event
import bcrypt


class User(db.Model):
    __tablename__ = "users"

    id = db.Column("id", db.Integer, primary_key=True)
    fullname = db.Column("fullname", db.Text)
    email = db.Column("email", db.Text)
    password = db.Column("password", db.Text)
    salt = db.Column("salt", db.Text)

    def __init__(self, fullname, email, password) -> None:
        """
        Initialize the user object and encode the password using bcrypt
        @param fullname - the user's full name.
        @param email - the user's email.
        @param password - the user's password
        """
        self.fullname = fullname
        self.email = email
        self.password = password

    def check_pwd(self, password) -> bool:
        """
        Check the password against the stored password.
        @param password - the password to check against the stored password.
        @returns True if the password is correct, False otherwise.
        """
        password_bytes = bytes(password, "utf-8")
        salt_bytes = bytes(self.salt, "utf-8")
        encrypted = bcrypt.hashpw(password_bytes, salt_bytes)

        return bcrypt.checkpw(password_bytes, encrypted)


@event.listens_for(User, "before_insert")
def before_user_insert(mapper, connect, target) -> None:
    """
    This function is called before a user is inserted into the database. It hashes the password with an auto-generated salt.
    @param mapper - the mapper for the database
    @param connect - the connection to the database
    @param target - the user being inserted
    """
    salt = bcrypt.gensalt(rounds=12)
    encoded = bytes(target.password, "utf-8")
    password = bcrypt.hashpw(encoded, salt)

    target.password = bytes.decode(password, "utf-8")
    target.salt = bytes.decode(salt, "utf-8")
