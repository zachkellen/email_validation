from flask_app import app
from flask import render_template, redirect, session, request, flash

from flask_app.models.email import Email

@app.route('/')
def index():
    print('Home')
    return render_template('submit.html')

@app.route('/submit' , methods=['POST'])
def create_email():
    if not Email.validate_email(request.form):
        return redirect('/')
    Email.create_email(request.form)
    return redirect('/success')

@app.route('/success')
def view_emails():
    emails = Email.get_all_emails()
    return render_template('success.html', emails = emails)