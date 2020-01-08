from flask import Flask, render_template, redirect, request, url_for
from forms import Questionnaire
import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase import Firebase

# FLASK APP INIT
app = Flask(__name__)
app.config.from_object('config.Config')

# FIREBASE STORAGE INIT
firebase = Firebase(app.config['FIREBASE_CONFIG'])
storage = firebase.storage()

# FIREBASE CLOUD DB INIT
cred = credentials.Certificate(app.config['FIREBASE_SERVICE_ACC_KEY'])
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()
doc_ref = db.collection(app.config['DB_NAME'])


    

@app.route('/', methods=['GET', 'POST'])
def get_form():
    form = Questionnaire()

    if request.method == "POST":
        
        client = form.company_name.data
        
        if form.logo.data:
            image = request.files['logo']
            storage.child('logos/'+ image.filename ).put(image.read())

           
            
            questionnaire = {
                'first_name': form.fname.data,
                'last_name': form.lname.data,
                'email': form.email.data,
                'phone_number': form.phone_number.data,
                'project_type': form.project_type.data,
                'company_name': form.company_name.data,
                'site_domain': form.domain.data,
                'about_company': form.about_company.data,
                'company_logo': form.company_logo.data,
                'logo': image.filename,
                'iot_description': form.iot_description.data,
                'database_description': form.database_description.data,
                'script_description': form.script_description.data,
                'webapp_description': form.webapp_description.data,
                'admin_page': form.admin_page.data,
                'custom_database': form.custom_database.data,
                'ui': form.ui.data,
                'website_description': form.intention.data,
                'home' : form.home.data,
                'about' : form.about.data,
                'contact' : form.contact.data,
                'gallery' : form.gallery.data,
                'events': form.events.data,
                'info' : form.info.data,
                'staff': form.staff.data,
                'other' : form.other.data,
                'other_section': form.other_section.data,
                'hosting' : form.hosting.data,
                'maintainence' : form.maintainence.data,
                'specifics' : form.specifics.data,
                'inspiration' : form.inspiration.data,
                'notes' : form.notes.data,
            }

            doc_ref.document(client).set(questionnaire)

            return redirect(url_for('message'))
        
        questionnaire = {
            'first_name': form.fname.data,
            'last_name': form.lname.data,
            'email': form.email.data,
            'phone_number': form.phone_number.data,
            'project_type': form.project_type.data,
            'company_name': form.company_name.data,
            'site_domain': form.domain.data,
            'about_company': form.about_company.data,
            'company_logo': form.company_logo.data,
            # 'logo': image.filename,
            'iot_description': form.iot_description.data,
            'database_description': form.database_description.data,
            'script_description': form.script_description.data,
            'webapp_description': form.webapp_description.data,
            'admin_page': form.admin_page.data,
            'custom_database': form.custom_database.data,
            'ui': form.ui.data,
            'website_description': form.intention.data,
            'home': form.home.data,
            'about': form.about.data,
            'contact': form.contact.data,
            'gallery': form.gallery.data,
            'events': form.events.data,
            'info': form.info.data,
            'staff': form.staff.data,
            'other': form.other.data,
            'other_section': form.other_section.data,
            'hosting': form.hosting.data,
            'maintainence': form.maintainence.data,
            'specifics': form.specifics.data,
            'inspiration': form.inspiration.data,
            'notes': form.notes.data,
            }

        doc_ref.document(client).set(questionnaire)
    
        return redirect(url_for('message'))

    return render_template('form.html', form=form)


@app.route('/thank_you')
def message():
    return render_template('thankYou.html')

