import os
from flask import Flask, render_template, request, redirect, url_for, session, flash
import mysql.connector

myDb = mysql.connector.connect(
    host="localhost",
    username="root",
    password="",
    database="cafe connect"
)

myCursor = myDb.cursor()

app = Flask(__name__)
app.secret_key = 'e-commerce'

def getProducts():
    myCursor.execute("SELECT * FROM products")
    myResult = myCursor.fetchall()
    return (myResult)

@app.route("/")

def index():
    return render_template('index.html')

@app.route("/product")
def product():
    product_list = getProducts()
    return render_template('product.html', product_list=product_list)

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        quantity = request.form['stock_quantity']
        category = request.form['category_id']
        myCursor.execute('INSERT INTO products (name, description, price, stock_quantity, category_id) VALUES (%s, %s, %s, %s, %s)',
        (name, description, price, quantity, category))
        myDb.commit()

        last_product_id = myCursor.lastrowid
        file_image_name = f"{last_product_id}.jpg"

        if 'file_image' not in request.files:
            flash("No File Part")
            return redirect(url_for('add_product'))

        file = request.files['file_image']

        if file.filename == '':
            flash("No Selected File.")
            return redirect(url_for('add_product'))

        if file:
            file.save(os.path.join('static/images', file_image_name))

        flash("Product added successfully!")
        return redirect(url_for('product'))


    return render_template('add_product.html')

@app.route('/login_register', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['rtxt']
        email = request.form['remail']
        password = request.form['rpswd']

        myCursor.execute('SELECT * FROM users WHERE email = %s AND password = %s', (email, password))
        users = myCursor.fetchone()

        if users:
            session['logged'] = True
            session['id'] = users[0]  # Assuming users[0] is the user ID
            session['email'] = users[2]  # Assuming users[1] is the email

            flash("Email already exists!")
            return redirect(url_for('add_user'))
        else:
            myCursor.execute('INSERT INTO users (name, email, password) VALUES (%s, %s, %s)',
                             (name, email, password))
            myDb.commit()

            flash("Registered Successfully!")
            return redirect(url_for('product'))
    return render_template('login_register.html')


@app.route('/login_user', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        email = request.form['semail']
        password = request.form['spswd']

        myCursor.execute('SELECT * FROM users WHERE email = %s AND password = %s', (email, password))
        users = myCursor.fetchone()

        if users:
            session['logged'] = True
            session['id'] = users[0]  # Assuming users[0] is the user ID
            session['email'] = users[2]  # Assuming users[1] is the email


            flash("Login Successful!")
            return redirect(url_for('add_product'))
        else:
            flash("Incorrect Email/Password.")
            return redirect(url_for('add_user'))

    return render_template('login.html')