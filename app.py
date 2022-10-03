from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# creating the database configurations
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://postgres:mark-115@localhost:5432/profileapp"
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template("index.html")