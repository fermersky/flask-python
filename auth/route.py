from flask import Blueprint, request
from auth.models import User
from app import db, executor
import time

from utils.mail_client import send_simple_message

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

    # executor.submit(send_simple_message)
    # send_simple_message.apply_async()
    # send_simple_message()

    end = time.perf_counter()

    elapsed = end - start
    print(elapsed)

    return f'login {request.args.get("id")} {elapsed}'
