from my_app import app
from flask import render_template, flash, redirect, url_for
from my_app.forms import LoginForm 

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
	form = LoginForm()
	if form.validate_on_submit():
		flash("Login requested for user {}, remember_me={}".format(form.username.data, form.remember_me.data))
		return redirect(url_for("index"))	

	return render_template("login.html", title="Sign In", form=form)
