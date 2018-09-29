from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'Key_Private'

@app.route('/')
def count():
    if session['count']:
        session['count'] +=1
    else:
        session['count'] = 1

    print(session['count'])
    print("hello")
    return render_template('index.html')

@app.route('/clear', methods = ['GET'])
def clear():
    session['count'] = 0
    return redirect('/')

@app.route('/double', methods = ['GET'])
def double():
    session['count'] +=1
    return redirect('/')

app.run(debug = True)