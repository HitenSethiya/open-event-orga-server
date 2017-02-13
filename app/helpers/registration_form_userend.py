from flask_wtf import Form
from wtforms import StringField, SelectField, DateField
from wtforms.validators import *
from wtforms.fields.html5 import TelField


class RegistrationForm(Form):
    firstname = StringField('First_Name', validators=[DataRequired()])
    lastname = StringField('Last_Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    email_confirm = StringField('Email_Confirm', validators=[DataRequired(), Email()])
    job_title = StringField('Job_Title', [validators.Length(min=3, max=30)])
    phone_no = TelField('Phone_no')
    work_phone = TelField('Work_Phone')
    mobile_phone = TelField('Mob_no')
    tax_business_info = StringField('Tax_Business_Info', validators=[DataRequired()])
    #billing_address = StringField('Billing_Address', validators=[Length(max=100)])
    home_address = StringField('Home_Address', validators=[Length(max=100)])
    work_address = StringField('Work_Address', validators=[Length(max=100)])
    shipping_address = StringField('Shipping_Address', validators=[Length(max=100)])
    organisation = StringField('Organisation', validators=[Length(max=50)])
    website = StringField('Website', validators=[Url()])
    blog = StringField('Blog', validators=[Url()])
    twitter = StringField('Twitter', validators=[Url()])
    facebook = StringField('Facebook', validators=[Url()])
    git_repo = StringField('Git_Repo', validators=[Url()])
    gender = SelectField('Gender', choices=[('M', 'Male'), ('F', 'Female'), ('U', 'Prefer Not to Declare')])
    dob = DateField('Date of Birth', format='%d/%m/%Y', validators=[Optional()])
# define auto-update function for fields if the user is logged in
# define a function to only display those fields that are selected by event creator
