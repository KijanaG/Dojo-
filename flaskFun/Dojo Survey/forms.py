from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('form.html')

@app.route('/result', methods = ['POST'])
def result():
    name = request.form['name']
    location = request.form['select']
    language = request.form['language']
    message = request.form['message']
    print(request)
    return render_template('result.html', name = name, location = location, language = language, message = message)

app.run(debug=True)
