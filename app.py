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
        
        client_name = form.fname.data[0] +'.'+ form.lname.data

        
        
        if request.files:
            image = request.files['logo']
            storage.child('logos/'+ image.filename ).put(image.read())
            
            questionnaire = {
                'fname': form.fname.data,
                'lname': form.lname.data,
                'email': form.email.data,
                'phone_number': form.phone_number.data,
                'company_name': form.company_name.data,
                'site_domain': form.domain.data,
                'about_company': form.about_company.data,
                'company_logo': form.company_logo.data,
                'logo': image.filename,
                'intention': form.intention.data,
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
                'specialties' : form.specialties.data,
                'inspiration' : form.inspiration.data,
                'notes' : form.notes.data,
            }

            doc_ref.document(client_name).set(questionnaire)

            return redirect(url_for('message'))
        
        questionnaire = {
                'fname': form.fname.data,
                'lname': form.lname.data,
                'email': form.email.data,
                'phone_number': form.phone_number.data,
                'company_name': form.company_name.data,
                'site_domain': form.domain.data,
                'about_company': form.about_company.data,
                'company_logo': form.company_logo.data,
                'intention': form.intention.data,
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
                'specialties' : form.specialties.data,
                'inspiration' : form.inspiration.data,
                'notes' : form.notes.data,
            }

        doc_ref.document(client_name).set(questionnaire)
    
        return redirect(url_for('message'))

    return render_template('form.html', form=form)


@app.route('/thank_you')
def message():
    return render_template('thankYou.html')

