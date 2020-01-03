from flask_wtf import FlaskForm
from wtforms import StringField, FileField, SubmitField, BooleanField, DecimalField , FileField, validators, IntegerField, PasswordField, TextAreaField
from wtforms.validators import InputRequired, Email



class Questionnaire(FlaskForm):
    fname = StringField('First Name',[InputRequired()])
    lname = StringField('Last Name', [InputRequired()])
    email = StringField('Email', [InputRequired(), Email('Please enter a valid email.')])
    phone_number = StringField('Phone Number')
    # PROJECT TYPE
    project_type = StringField('Project Type')
    # ABOUT THE COMPANY
    domain = StringField('Site Domain')
    company_name = StringField('Company/Organization Name')
    about_company = TextAreaField('About Company')
    company_logo = BooleanField('Do you have a logo?')
    logo = FileField('Upload Logo')
    # ABOUT THE PROJECT
    script_description = TextAreaField('Please describe the what you want the program to do to the best of your ability.')
    webapp_description = TextAreaField('Please describe your idea to the best of your ability.')
    admin_page = BooleanField('Do you need an admin page?')
    custom_database = BooleanField('Will you require a custom database?')
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

