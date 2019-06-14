from flask_wtf import FlaskForm 
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.fields.html5 import DateField
from wtforms.validators import InputRequired, Email, Length, DataRequired, ValidationError
from dnd.models import User, Interest, Article

# Login Form
class LoginForm(FlaskForm):

    username = StringField('Username', validators=[InputRequired()], render_kw={'autofocus': True})
    password = PasswordField('Password', validators=[InputRequired()])
    remember = BooleanField('Remember Me')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if not user:
            raise ValidationError('Username does not exists. Maybe try a different one.')

    def validate_password(self, password):
        user = User.query.filter_by(username=self.username.data).first()
        if user and not check_password_hash(user.password, self.password.data):
            raise ValidationError('Password incorrect. Please choose a different one.')

# Register Form
class RegisterForm(FlaskForm):

    first_name = StringField('First Name', validators=[InputRequired(), Length(min=4, max=15)], render_kw={'autofocus': True})
    last_name = StringField('Last Name', validators=[InputRequired(), Length(min=4, max=15)])
    date_of_birth = DateField('Date of Birth', format="%Y-%m-%d", validators=[DataRequired()])
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('Remember Me')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exists. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already exists. Please choose a different one.')

class UpdateUserInterestsForm(FlaskForm):
    interest_1 = StringField('Interest 1', validators=[DataRequired()])
    interest_2 = StringField('Interest 2', validators=[DataRequired()])
    interest_3 = StringField('Interest 3', validators=[DataRequired()])
    submit = SubmitField('Update')