from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    print("MAIN WORKING")
    return render_template('index.html', name = 'YOLO')


@app.route('/dojo')
def dojo():
    print("DOJO WORKING")
    return "Dojo!!!"

@app.route('/flask')
def flask():
    print("FLASK WORKING")
    return "<input type='button', name='SUUHHH FLASK'>Suuhhh FLAsKIE </>"

@app.route('/michael')
def michael():
    print("MJJJJJJ")
    return "<h6> OUTCHeEEeEE </h6>"

@app.route('/john')
def john():
    print("JOHNNY")
    return "JOhn E Boi "

@app.route('/repeat/<num>/<nameput>')
def hello(num, nameput):
    print("ACTIVATE***MATRIX***"*80)
    return ("<p>"+nameput+"</p>")*int(num)

app.run(debug = True)