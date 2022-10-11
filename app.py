from flask import Flask, render_template, url_for, request, session, redirect
from flask_sqlalchemy import SQLAlchemy

# Declaring the flask application object...
app = Flask(__name__)
# setting the session secret
app.secret_key = 'my secret key'

# creating the database configurations
# the conventions for the URI of a postgres db is postgres://username:password@server:port/databaseName
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:mark-115@localhost:5432/profileapp"
db = SQLAlchemy(app)
# the profile table
class userProfile(db.Model):
    __tablename__ = "profile" # the tablename 

    # The table data 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    date_of_birth = db.Column(db.Date)
    email = db.Column(db.String, unique=True)
    country = db.Column(db.String)
    gender = db.Column(db.String)
    interest = db.Column(db.Text)
    skills = db.Column(db.Text)

# creating all the objects on the table.. 
db.create_all()

@app.route('/') # the home page route
def index():
    return render_template("index.html")

@app.route('/create-account', methods=["GET", "POST"])
def create_account():  # the account creation page route
    if request.method == 'POST':
        session['name'] = request.form.get('fullname')
        session['email'] = request.form.get('email')
        session['date'] = request.form.get('dateofbirth')
        session['country'] = request.form.get('country')
        session['skills'] = request.form.get('skills')
        session['gender'] = request.form.get('gender')
        session['interest'] = request.form.get('interest')
        session['other'] = request.form.get('other')
        user = userProfile(name=session.get('name'), date_of_birth=session.get('dateofbirth'), email=session.get('email'), 
        country=session.get('country'), gender=session.get('gender'), interest=session.get('interest'), skills=session.get('skills'))
        db.session.add(user)
        return redirect('/profile-report-page')
    return render_template('create_account.html')


# the next step is to give the user a report that the account has been created
@app.route('/profile-report-page')  # the report page app
def accountReport():
    name = session.get('name')
    page_title = "Account Created"
    message=f'Congratulations {name} for taking this first step. You have Successfully created your account'
    link_text = "View your Profile"
    return render_template('reporttemplate.html', pagetitle=page_title, pagecontent=message, linktext=link_text)

@app.route('/profile')
def user_profile():
    return 'profile page random text'