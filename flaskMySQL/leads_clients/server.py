from flask import Flask, render_template, request, redirect
# import the function connectToMySQL from the file mysqlconnection.py
from mysqlconnection import connectToMySQL
app = Flask(__name__)
# invoke the connectToMySQL function and pass it the name of the database we're using
# connectToMySQL returns an instance of MySQLConnection, which we will store in the variable 'mysql'
mysql = connectToMySQL('lead_gen_business')
# now, we may invoke the query_db method
@app.route('/')
def index():
    client_list = mysql.query_db("SELECT clients.client_id AS 'id', clients.first_name, clients.last_name, COUNT(leads.leads_id) AS 'Total_Leads' FROM clients JOIN sites ON sites.client_id = clients.client_id JOIN leads ON sites.site_id = leads.site_id GROUP BY clients.client_id ORDER BY clients.client_id ASC;")

    return render_template('index.html', client = client_list)

if __name__ == "__main__":
    app.run(debug=True)
