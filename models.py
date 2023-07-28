"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""

    app.app_context().push()
    db.app = app
    db.init_app(app)

DEFAULT_IMAGE_URL = "https://tinyurl.com/defaultprofile12344645"


class User(db.Model):

    __tablename__= "users"

    id = db.Column(
        db.Integer,
        primary_key = True,
        autoincrement = True
    )

    first_name = db.Column(
        db.String(50),
        nullable = False
    )

    last_name = db.Column(
        db.String(50),
        nullable = False
    )

    image_url = db.Column(
        db.String(300),  #TODO: change to text
        nullable=True,
        default=DEFAULT_IMAGE_URL  #TODO: Don't have this with nullable = True
    )


class Post(db.Model):

    __tablename__= "posts"

    id= db.Column(
        db.Integer,
        primary_key= True,
        autoincrement = True
    )

    title = db.Column(
        db.String(50),
        nullable = False
    )

    content = db.Column(
        db.Text(),
        nullable = False
    )

    created_at = db.Column(
        db.DateTime,
        nullable = False,
        default = db.func.now()
    )

    user = db.Column(
        db.Integer,
        db.ForeignKey('users.id')
    )

    user = db.relationship('User', backref = 'posts')