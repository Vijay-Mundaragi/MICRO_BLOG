from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length
from my_app.models import User


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

    