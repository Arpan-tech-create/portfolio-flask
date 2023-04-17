from flask import Flask,jsonify,render_template,request
import mysql.connector
import nbformat
from nbconvert import HTMLExporter

app=Flask(__name__,template_folder='templates')


@app.route("/")
def home():

    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():

    name = request.form['cf-name']
    email = request.form['cf-email']
    message = request.form['cf-message']

 
    cnx = mysql.connector.connect(user='root', password='mysqlinstaller@001', host='localhost', database='portfolio',port=3305)
    cursor = cnx.cursor()

   
    insert_query = "INSERT INTO contacts (name, email, message) VALUES (%s, %s, %s)"
    cursor.execute(insert_query, (name, email, message))

    
    cnx.commit()
    cursor.close()
    cnx.close()

    return render_template('success.html')

@app.route("/notebook")
def show_notebook():
 

    return render_template('note.html')

@app.route("/note")
def show_notebook1():
 

    return render_template('note1.html')

@app.route("/note21")
def show_notebook2():
 

    return render_template('note2.html')

@app.route("/gallery")
def gal():
 

    return render_template('gallery1.html')

app.run(debug=True)