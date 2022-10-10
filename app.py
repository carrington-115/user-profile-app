from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# creating the database configurations
# the conventions for the URI of a postgres db is postgres://username:password@server:port/databaseName
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://postgres:mark-115@localhost:5432/profileapp"
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/create-account', methods=["GET", "POST"])
def create_account():
    return render_template('create_account.html')

@app.route('/profile')
def user_profile():
    return render_template('profile_page')