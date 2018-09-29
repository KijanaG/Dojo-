from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'l0w~k3y'

@app.route('/')
def count():
    if 'count' in session == None:
        session['count'] = 0
    if 'update' in session == None:
        session['update'] = []
    return render_template('index.html')


@app.route('/process_money', methods = ['POST'])
def process_money():
    #FARM
    if 'farm' in request.form:
        session['farm'] = random.randrange(10, 21)
        session['count']+=session['farm']
        val = "Earned " + str(session['farm']) + " golds from the farm!" + " (" +str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))+ ")"    
        session['update'].append(val)
        print(session['count'], session['farm'])
    #CAVE
    elif 'cave' in request.form:
        session['cave'] = random.randrange(5, 11)
        session['count']+=session['cave']
        val = "Earned " + str(session['cave']) + " golds from the cave!" + " (" +str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + ")"        
        session['update'].append(val)
        print(session['count'], session['cave'])
    #HOUSE
    elif 'house' in request.form:
        session['house'] = random.randrange(2, 6)
        session['count']+=session['house']
        val = "Earned " + str(session['house']) + " golds from the house!" + " (" +str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + ")"        
        session['update'].append(val)
        print(session['count'], session['house'])
    #CASINO
    elif 'casino' in request.form:
        session['casino'] = random.randrange(0, 51)
        if session['casino'] %2 ==0:
            session['count'] -= session['casino']
            val = "Entered a casino and lost " + str(session['casino']) + " golds ... Ouch!" +" (" + str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))+ ")"
            session['update'].append(val)
        elif session['casino'] %2 !=0:
            session['count']+=session['casino']
            val = "Entered a casino and won " + str(session['casino']) + " golds ... YES!" + " (" +str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + ")"            
            session['update'].append(val)
        print(session['count'], session['casino'])
    return redirect('/')


if __name__ == "__main__":
    app.run(debug = True)