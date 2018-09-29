from flask import Flask, render_template

app = Flask(__name__)

@app.route('/sjsweets')
def table():
    students = (
        {'first_name': 'Susan', 'last_name': 'Swerdloff'},
        {'first_name': 'KJ', 'last_name': 'Garrett'},
        {'first_name': 'Mark', 'last_name': 'Guillen'},
        {'first_name': 'KB', 'last_name': 'Tonel'}
    )
    return render_template('table.html', students = students)

app.run(debug = True)