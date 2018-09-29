from flask import Flask, render_template, request, redirect, session, flash, session
import re
from mysqlconnection import connectToMySQL

app = Flask(__name__)
app.secret_key = "flowkey"

mysql = connectToMySQL('email_val')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/process', methods=['POST'])
def process():
    email = request.form['email']
    find_user = mysql.query_db("SELECT * FROM emails WHERE email = %(email)s", {'email': email})
    email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    if len(email) == 0:
        flash(u'Email cannot be blank.','error')
        return redirect('/')
    elif not email_regex.match(email):
        flash(u'Invalid Email Address','error')
        return redirect('/')
    else:
        pass
    if len(find_user) > 0:
        flash(f'Email: {email} is already taken', 'error')
        return redirect('/')
    else:
        mysql.query_db("INSERT INTO emails (email, created_at, updated_at) VALUES(%(email)s, NOW(), NOW())", {'email': email})
        return redirect('/forum')

@app.route('/forum')
def another():
    display_users = mysql.query_db("SELECT * FROM emails;")
    return render_template('index.html', users = display_users)

@app.route('/delete', methods=['POST'])
def delete():
    user = request.form['hidden']
    mysql.query_db(f"DELETE FROM emails WHERE id = {user}")
    return redirect('/forum')

if __name__ == "__main__":
    app.run(debug = True)
