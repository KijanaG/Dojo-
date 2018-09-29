from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = "dskldfj"
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
    if len(name) <= 2:
        flash("Name must be longer than 2 characters.")
        return redirect('/')
    elif not name.isalpha():
        flash("Only characters A-Z work here, sorry!")
        return redirect('/')
    if len(message) > 120:
        flash("Message cannot be longer than 120 characters.")
        return redirect('/')
    elif len(message) <1:
        flash("No message?! :-(((")
        return redirect('/')
    return render_template('result.html', name = name, location = location, language = language, message = message)

app.run(debug=True)
