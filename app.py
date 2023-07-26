"""Blogly application."""


import os

from flask import Flask, render_template, request
from models import connect_db, User, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", 'postgresql:///blogly')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

USERS_LIST = []


@app.get("/")
def go_to_users():
    return "Hello"
    # return redirect


@app.get("/users")
def show_users():
    """Show homepage with users with add user button"""

    return render_template("users.html", users = USERS_LIST)




