from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
	# the fields of the form are represented as class variables
	username = StringField("User Name", validators=[DataRequired()]) # validators arg is list => can assign more than one validator to a field
	password = PasswordField("Password", validators=[DataRequired()])
	remember_me = BooleanField("Remember Me")
	submit = SubmitField("Sign In")