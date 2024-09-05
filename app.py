from flask import Flask, render_template, url_for, flash, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "My Secret Key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'

db = SQLAlchemy(app)


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(120), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    post = db.Column(db.Text, nullable=False)
    time_created = db.Column(db.DateTime, default=datetime.utcnow)


class PostForm(FlaskForm):
	name = StringField('Name', validators=[DataRequired()])
	post = TextAreaField('Post', validators=[DataRequired()],widget=TextArea())
	title = StringField('Title', validators=[DataRequired()])
	submit = SubmitField('Submit')

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/create_post', methods=["POST", "GET"])
def create_post():
	form = PostForm()
	if form.validate_on_submit():
		name = form.name.data
		post = form.post.data
		title = form.title.data
		post_created = Posts(name=name, post=post, title=title)
		db.session.add(post_created)
		db.session.commit()
		flash(f'Hi {name}. You posted succesfully!!', 'success')	
		return redirect('posts')
	return render_template('create_post.html', form=form)

@app.route('/posts')
def posts():
	all_posts = Posts.query.order_by(Posts.time_created).all()
	return render_template("posts.html", all_posts=all_posts)

@app.route('/delete/<int:id>')
def delete_post(id):
	post_to_delete = Posts.query.get_or_404(id)
	db.session.delete(post_to_delete)
	db.session.commit()
	flash(f"Post {id} deleted!!", 'danger')
	return redirect(url_for('posts'))

@app.route('/update/<int:id>', methods=["POST", "GET"])
def update_post(id):
	post_to_update = Posts.query.get_or_404(id)
	form = PostForm(name=post_to_update.name, title=post_to_update.title, post=post_to_update.post)
	if form.validate_on_submit():
		post_to_update.name = form.name.data
		post_to_update.title = form.title.data
		post_to_update.post = form.post.data
		db.session.commit()
		flash(f'You updated!!', 'warning')	
		return redirect(url_for('posts'))
	return render_template("update_post.html", form=form, post_to_update=post_to_update)
		






if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0", port=5000)