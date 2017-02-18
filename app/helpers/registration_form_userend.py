from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateField, TextAreaField
from wtforms.validators import *
from wtforms.fields.html5 import TelField


class RegistrationForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email(), EqualTo('email_confirm', message='Passwords must match')])
    email_confirm = StringField('Confirm Email', validators=[DataRequired(), Email()])
    job_title = StringField('Job Title', validators=[Length(min=3, max=30)])
    phone_no = TelField('Phone no')
    work_phone = TelField('Work Phone')
    mobile_phone = TelField('Mob no')
    tax_business_info = StringField('Tax and Business Info', validators=[DataRequired()])
    #billing_address = StringField('Billing_Address', validators=[Length(max=100)])
    home_address = TextAreaField('Home Address', validators=[Length(max=100)])
    work_address = TextAreaField('Work Address', validators=[Length(max=100)])
    shipping_address = TextAreaField('Shipping Address', validators=[Length(max=100)])
    organisation = StringField('Organisation', validators=[Length(max=50)])
    website = StringField('Website', validators=[URL()])
    blog = StringField('Blog', validators=[URL()])
    twitter = StringField('Twitter', validators=[URL()])
    facebook = StringField('Facebook', validators=[URL()])
    git_repo = StringField('Main Git Repository', validators=[URL()])
    gender = SelectField('Gender', choices=[('M', 'Male'), ('F', 'Female'), ('U', 'Prefer Not to Declare')])
    dob = DateField('Date of Birth', format='%d/%m/%Y', validators=[Optional()])


# define auto-update function for fields if the user is logged in
# define a function to only display those fields that are selected by event creator
