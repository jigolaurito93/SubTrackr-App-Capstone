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
    subscription = SelectField('Name of Subscription', validators=[InputRequired()], choices=[('option1', 'Amazon Prime'), ('option2', 'Audible'), ('option3', 'Costco'), ('option4', 'Disney+'), ('option5', 'DoorDash'), ('option 6', 'Electricity'), ('option 7', 'HBO Max'), ('option 8', 'Hello Fresh'), ('option 9', 'Hulu'), ('option 10', 'Netflix'), ('option 11', 'Pandora'), ('option 12', 'Playstation Plus'), ('option 13', 'Rent'), ('option 14', 'Spotify'), ('option 15', 'Uber'), ('option 16', 'Youtube Premium'), ('option 17', 'other')])
    other = StringField('Other', validators=[InputRequired()])
    # TextareaField is a form field that can accept multiline text.
    # amount = DecimalField('Amount', places=2, rounding=ROUND_HALF_UP )
    amount = DecimalField('Amount', places=2, validators=[InputRequired()] )
    date = DateField('Subscription Date', validators=[InputRequired()])
    frequency = SelectField('Payment Frequency', choices=[('option1', 'Daily'), ('option2', 'Weekly'), ('option3', 'Bi-weekly'), ('option4', 'Semi-monthly'), ('option5', 'Monthly'), ('option 6', 'Quarterly'), ('option 7', 'Semi-annually'), ('option 8', 'Annually')], validators=[InputRequired()])
    image_url = StringField('Image URL')
    submit = SubmitField('Subscribe')