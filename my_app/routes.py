from my_app import app
from flask import render_template, flash, redirect, url_for
from flask_login import login_user,current_user
from my_app.forms import LoginForm
from my_app.models 


@app.route("/")
@app.route("/index")
def index():
	user = {"name":"Vijay"}
	posts = [
		{
			"author":{"username": "Harvey Specter"},
			"body":"I dont play the odds..... I play the man"
		},
		{
			"author":{"username": "Mike Ross"},
			"body":"You put your interests above mine.... I'm putting them back up next to yours!...Boom!!!"
		}
	]
	return render_template("index.html", title="Home", user=user, posts=posts)

@app.route("/login", methods=["GET", "POST"])
def login():
	if current_user.is_authenticated:
		return redirect(url_for("index"))
	form = LoginForm()
	if form.validate_on_submit():
		# flash("Login requested for user {}, remember_me={}".format(form.username.data, form.remember_me.data))
		user = User.query.filter_by(username=form.username.data).first()
		if user is None or user.check_password(form.password.data):
			flash("Invalid username or password")
			return redirect(url_for("login"))
		login_user(user, remember=form.remember_me.data) 
		return redirect(url_for("index"))

	return render_template("login.html", title="Sign In", form=form)
