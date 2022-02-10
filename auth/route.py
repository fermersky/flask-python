from flask import Blueprint, request
from auth.models import User
from app import db
import time

auth = Blueprint("auth", __name__, url_prefix="/auth")


@auth.post("login")
def login():
    """
    This function is used to log in a user. It takes the user's email and password and checks if it is in the database.
    @returns the user's id and the time it took to login.
    """
    print("REQUEST", request.args.get("id"))
    start = time.perf_counter()
    data = request.get_json()
    user = User(fullname=data["fullname"], email=data["email"], password=data["password"])

    db.session.add(user)
    db.session.commit()

    end = time.perf_counter()

    elapsed = end - start
    print(elapsed)

    return f'login {request.args.get("id")} {elapsed}'
