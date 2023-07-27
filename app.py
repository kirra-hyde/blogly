"""Blogly application."""


import os

from flask import Flask, render_template, request, redirect
from models import connect_db, User, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", 'postgresql:///blogly')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)



@app.get("/")
def go_to_users():
     return redirect("/users")


@app.get("/users")
def show_users():
    """Show homepage with users with add user button"""
    users = User.query.all()
    return render_template("users.html", users=users )

@app.get("/users/new")
def user_form():
    """show new user form """
    return render_template("user_new.html")


@app.post("/users/new")
def add_user():
    firstname = request.form["firstname"]
    lastname = request.form["lastname"]
    image = request.form.get("imageurl")

    user = User(first_name=firstname, last_name=lastname, image_url=image)
    db.session.add(user)
    db.session.commit()

    return redirect("/users")

@app.get("/users/<int:user_id>")
def show_individual_user(user_id):
    """Show info of user on a single post"""
    user = User.query.get_or_404(user_id)
    return render_template("user_details.html", user=user)


@app.get("/users/<int:user_id>/edit")
def show_edit_page(user_id):
    """Show form to edit user info"""
    user = User.query.get_or_404(user_id)
    return render_template("user_edit.html",user=user)


@app.post("/users/<int:user_id>/edit")
def edit_profile(user_id):
    """Update user info"""

    firstname = request.form["firstname"]
    lastname = request.form["lastname"]
    image = request.form.get("imageurl")

    user = User.query.filter(User.id == user_id).first()
    user.first_name = firstname
    user.last_name = lastname
    user.image_url = image

    db.session.commit()

    return redirect("/users")

