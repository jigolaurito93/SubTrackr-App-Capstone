from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, DateField, DecimalField, SelectField
from wtforms.validators import EqualTo, InputRequired

subs = ['Netflix', 'Gmail', 'Yahoo']


class SignUpForm(FlaskForm):
    first_name = StringField('First Name', validators=[InputRequired()])
    last_name = StringField('Last Name', validators=[InputRequired()])
    username = StringField('Username', validators=[InputRequired()])
    email = EmailField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    confirm_pass = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Log in')

class PostForm(FlaskForm):
    subscription = SelectField('Name of Subscription', validators=[InputRequired()], choices=[('Amazon Prime', 'Amazon Prime'), ('Audible', 'Audible'), ('Costco', 'Costco'), ('Disney+', 'Disney+'), ('DoorDash', 'DoorDash'), ('Electricity', 'Electricity'), ('HBO Max', 'HBO Max'), ('Hello Fresh', 'Hello Fresh'), ('Hulu', 'Hulu'), ('Netflix', 'Netflix'), ('Pandora', 'Pandora'), ('Playstation Plus', 'Playstation Plus'), ('Rent', 'Rent'), ('Spotify', 'Spotify'), ('Uber', 'Uber'), ('Youtube Premium', 'Youtube Premium'), ('other', 'other')])
    # otherfield = StringField('Other')
    # TextareaField is a form field that can accept multiline text.
    # amount = DecimalField('Amount', places=2, rounding=ROUND_HALF_UP )
    amount = DecimalField('Amount', places=3, validators=[InputRequired()] )
    date = DateField('Subscription Date', validators=[InputRequired()])
    frequency = SelectField('Payment Frequency', choices=[('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Bi-weekly', 'Bi-weekly'), ('Semi-monthly', 'Semi-monthly'), ('Monthly', 'Monthly'), ('Quarterly 6', 'Quarterly'), ('Semi-annually', 'Semi-annually'), ('Annually', 'Annually')], validators=[InputRequired()])
    image_url = StringField('Image URL')
    submit = SubmitField('Subscribe')