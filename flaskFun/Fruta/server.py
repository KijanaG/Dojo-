from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    strawberry = request.form['strawberry']
    blackberry = request.form['blackberry']
    raspberry = request.form['raspberry']
    apple = request.form['apple']
    fname = request.form['first_name']
    lname = request.form['last_name']
    iden = request.form['iden']
    print(request.form)
    return render_template("checkout.html", strawberry = int(strawberry), blackberry = int(blackberry), raspberry = int(raspberry), apple = int(apple), fname = fname, lname = lname, iden = iden)

@app.route('/fruits')         
def fruits():
    print(request)
    print("**"*15)
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    