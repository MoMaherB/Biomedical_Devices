from flask import Flask, render_template, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired


app = Flask(__name__)

app.config["SECRET_KEY"] = "secret"
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///portfolio.db'

db = SQLAlchemy(app)

class UserForm(FlaskForm):
	user_name = StringField("User Name", validators=[DataRequired()])
	password = PasswordField("Password", validators=[DataRequired()])
	submit = SubmitField("Log In")

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True) 
	user_name = db.Column(db.String(120), nullable=False, unique=True)
	password = db.Column(db.String(120), nullable=False)


	def __repr__(self):
		return f"User Name: {self.user_name}. Password: {self.password}"
	


@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html')


@app.route('/login', methods=["GET", "POST"])
def login():
	form = UserForm()
	if form.validate_on_submit():
		user = User.query.filter_by(user_name=form.user_name.data).first()
		if user:
			if user.password == form.password.data:
				flash("You are logged in successfuly", "success")
				return redirect('/dashboard')
			else:
				flash("Wrong Password. Please try again!", "danger")
				return redirect(url_for('login'))
		else:
			flash("Wrong Username. Please try again!", "danger")
			return redirect(url_for('login'))
		
	return render_template('/login.html', form=form)

@app.route('/dashboard')
def dashboard():
	return render_template("dashboard.html")

@app.route('/departments')
def departments():
	return render_template("departments.html")

@app.route('/about')
def about():
	return render_template("about.html")

if __name__ == "__main__":
	app.run(debug=True)