from flask_wtf import FlaskForm
from wtforms import StringField, FileField, SubmitField, BooleanField, DecimalField , FileField, validators, IntegerField, PasswordField, TextAreaField
from wtforms.validators import InputRequired, Email



class Questionnaire(FlaskForm):
    fname = StringField('First Name',[InputRequired()])
    lname = StringField('Last Name', [InputRequired()])
    email = StringField('Email', [InputRequired(), Email('Please enter a valid email.')])
    phone_number = StringField('Phone Number')
    # ABOUT THE COMPANY
    domain = StringField('Site Domain')
    company_name = StringField('Company/Organization Name')
    about_company = TextAreaField('About Company')
    company_logo = BooleanField('Do you have a logo?')
    logo = FileField('Upload Logo')
    # ABOUT THE PROJECT
    intention = TextAreaField('What is the purpose of the website?')
    home = BooleanField()
    about = BooleanField()
    contact = BooleanField()
    gallery = BooleanField()
    events = BooleanField()
    info = BooleanField()
    staff = BooleanField()
    other = BooleanField()
    other_section = StringField('Enter other Section/Page')
    hosting = BooleanField('Will you need web hosting?')
    maintainence = BooleanField('Will you need site maintainence?')
    specialties = TextAreaField('Would you like any special features/functionality?')
    inspiration = StringField('Please list any websites that inspire your vision.')
    notes = TextAreaField('Extra Notes or Info..')
    submit = SubmitField('Submit')

