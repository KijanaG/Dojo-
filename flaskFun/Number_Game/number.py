from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'Key_Private'

@app.route('/')
def count():
    if session['random'] == None:
        session['random'] = random.randrange(0, 101)
    return render_template('index.html')

@app.route('/guess', methods = ['POST'])
def huuuu():
    session['number'] = int(request.form['number'])
    var = session['number']
    print(session['random'], session['number'])
    session['correct'] = False
    if var > session['random']:
        session['answer'] = "Too High"
        print("Too High")
    elif var == session['random']:
        session['answer'] = "Perfect! Play Again?"
        session['correct'] = True
        print("YES")
    else:
        session['answer'] = "Too Low"
        print("Too HE")
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['random'] = None
    session['correct'] = False
    session['answer'] = ""
    return redirect('/')
app.run(debug = True)