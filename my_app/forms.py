from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length
from my_app.models import User

class LoginForm(FlaskForm):
	# the fields of the form are represented as class variables
	username = StringField("User Name", validators=[DataRequired()]) # validators arg is list => can assign more than one validator to a field
	password = PasswordField("Password", validators=[DataRequired()])
	remember_me = BooleanField("Remember Me")
	submit = SubmitField("Sign In")

class RegistrationForm(FlaskForm):
	
	username = StringField("User Name", validators=[DataRequired()])
	email = StringField("Email", validators=[DataRequired(), Email()])
	password = PasswordField("Password", validators=[DataRequired()])
	password2 = PasswordField("Repeat Password", validators=[DataRequired(), EqualTo("password")])
	submit = SubmitField("Register")

	#custom validators
	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user is not None:
			raise ValidationError("Please use a different username")


	def validate_email(self, email):
		mail = User.query.filter_by(email=email.data).first()
		if mail is not None:
			raise ValidationError("Please use a different email address")

class EditProfileForm(FlaskForm):
	username = StringField("User Name", validators=[DataRequired()])
	about_me = TextAreaField("About me:", validators=[Length(min=0, max=140)])
	submit = SubmitField("Submit")

	def __init__(self, original_username):
		super(EditProfileForm, self).__init__()
		self.original_username = original_username

	def validate_username(self, username):
		if username.data != self.original_username:
			user = User.query.filter_by(username=username.data).first()
			if user is not None:
				raise ValidationError("Please use a different username")
				


class PostForm(FlaskForm):
	post = TextAreaField("Write Something here....", validators=[DataRequired(), Length(min=1, max=140)])
	submit = SubmitField("Submit")
