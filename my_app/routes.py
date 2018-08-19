from my_app import app
from flask import render_template

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