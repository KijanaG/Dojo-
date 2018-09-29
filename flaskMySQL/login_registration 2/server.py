from flask import Flask, render_template, redirect, request, session, flash
import re
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key="klfjds"

mysql = connectToMySQL('login')

@app.route('/')
def main():
    session['first_name'] = None
    session['userid']
    return render_template('index.html')

@app.route('/process', methods = ['POST'])
def verify():
    valid = True
    f_name = request.form['first_name']
    if not f_name.isalpha():
        flash(u'Name must be letters only.','haters')
        valid = False
    elif len(f_name) <=2 and len(f_name) > 0:
        flash(u'Name must be longer than two characters.','haters')
        valid = False
    elif len(f_name) == 0:
        flash(u'First Name needs input.','haters')
        valid = False
    else:
        pass
    l_name = request.form['last_name']
    if not l_name.isalpha():
        flash(u'Name must be letters only.','last')
        valid = False
    elif len(l_name) <=2 and len(l_name) > 0:
        flash(u'Name must be longer than two characters.','last')
        valid = False
    elif len(l_name) == 0:
        flash(u'Last Name needs input.','last')
        valid = False
    else:
        pass
    email = request.form['email']
    email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    if len(email) == 0:
        flash(u'Email cannot be blank.','mail')
        valid = False
    elif not email_regex.match(email):
        flash(u'Invalid Email Address','mail')
        valid = False
    else:
        pass
    passw = request.form['password']
    uppercase = 0
    number = 0
    for i in passw:
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
   ############################################################     
    find_user = mysql.query_db("SELECT * FROM users WHERE email = %(email)s;",{'email': email})
    print(find_user)
    if find_user and len(find_user) > 0:
        flash('Email is already taken', 'mail')
        return redirect('/')
    else:
        pw_hash = bcrypt.generate_password_hash(passw)
        print(pw_hash)
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at, hash) VALUES (%(f_name)s, %(l_name)s, %(email)s, NOW(), NOW(), %(pw_hash)s);"
        data = {"f_name": request.form['first_name'],
                "l_name": request.form['last_name'],
                "email": request.form['email'],
                "pw_hash": pw_hash}
        mysql.query_db(query, data)
        current_user = mysql.query_db("SELECT * FROM users WHERE email = %(email)s;",{'email': email})
        session['userid'] = current_user[0]['id'] 
        session['first_name'] = f_name
        return redirect('/success')


@app.route('/success')
def success():
    if 'first_name' in session == None:
        return redirect('/')
    return render_template('logged_in.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    query = "SELECT * FROM users WHERE email = %(email)s;"
    data = {"email": email}
    find_user = mysql.query_db(query, data)
    pw_hash = bcrypt.generate_password_hash(password)
    print("HELLOOOO")
    if find_user:
        print("GOOODBYYEEE")
        if bcrypt.check_password_hash(find_user[0]['hash'], password):
            print("YOOLLOOO")
            session['userid'] = find_user[0]['id']
            session['first_name'] = find_user[0]['first_name']
            return redirect('/success')
    flash(u'You could not be logged in', 'login')
    return redirect('/')

app.run(debug=True)