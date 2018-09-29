from flask import Flask, render_template, redirect, request, session, flash
import re
app = Flask(__name__)
app.secret_key="klfjds"

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/process', methods = ['POST'])
def verify():
    valid = True
    f_name = request.form['first_name']
    if not f_name.isalpha():
        flash(u'Name must be letters only.','error')
        valid = False
    elif len(f_name) <=2 and len(f_name) > 0:
        flash(u'Name must be longer than two characters.','error')
        valid = False
    elif len(f_name) == 0:
        flash(u'First Name needs input.','error')
        valid = False
    else:
        pass
    l_name = request.form['last_name']
    if not l_name.isalpha():
        flash(u'Name must be letters only.','error')
        valid = False
    elif len(l_name) <=2 and len(l_name) > 0:
        flash(u'Name must be longer than two characters.','error')
        valid = False
    elif len(l_name) == 0:
        flash(u'Last Name needs input.','error')
        valid = False
    else:
        pass
    email = request.form['email']
    email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    if len(email) == 0:
        flash(u'Email cannot be blank.','error')
        valid = False
    elif not email_regex.match(email):
        flash(u'Invalid Email Address','error')
        valid = False
    else:
        pass
    passw = request.form['password']
    password = passw.split()
    uppercase = 0
    number = 0
    for i in password:
        if i.isupper():
            uppercase +=1
        elif i.isdigit():
            number +=1
    if uppercase == 0:
        flash(u'Password must have at least one capital letter','error')
        valid = False
    elif number == 0:
        flash(u'Password must have at least one number','error')
        valid = False
    else:
        pass
    if len(request.form['password']) < 8:
        flash(u'Password must be at least 8 characters.','error')
        valid = False
    elif request.form['password'] != request.form['confirm']:
        flash(u'Passwords Must Match.','error')
        valid = False
    elif (len(request.form['password']) or len(request.form['confirm'])) == 0:
        flash(u'Password must be filled out','error')
        valid = False
    else: 
        pass
    if valid == False:
        return redirect('/')
    else:
        return 'Thank you for submitting!'

app.run(debug=True)