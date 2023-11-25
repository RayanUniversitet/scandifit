# from flask import Blueprint, render_template

from flask import Blueprint, render_template, request, session, redirect
from db import cursor, db
from flask_mail import Mail, Message
from db import mail

views = Blueprint('views', __name__)

@views.route("/")
def home():
    #to show add to card info
    product_info = None
    if 'product-id' in session:
        ids = session['product-id']
        cursor.execute('SELECT * FROM products WHERE id IN %s', (ids,))
        product_info = cursor.fetchall()
    return render_template('index.html', product_info=product_info)

@views.route("/send-message", methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        namn = request.form.get('namn')
        email = request.form.get('email')
        meddelande = request.form.get('meddelande')
        
        # for mail sending 
        msg = Message('Vi Har Tagit Emot Ditt Medelande', recipients=[email, 'kontakta@scandifit.se'])
        msg.html = render_template('mail_contact.html', namn=namn, meddelande=meddelande)
        mail.send(msg)  # Use 'mail', not 'Mail'
        return redirect(request.referrer)

@views.route("/jobb")
def jobb():
    #to show add to card info
    product_info = None
    if 'product-id' in session:
        ids = session['product-id']
        cursor.execute('SELECT * FROM products WHERE id IN %s', (ids,))
        product_info = cursor.fetchall()

    return render_template('jobb.html', product_info=product_info)

@views.route("/signup")
def signup():
    return render_template('login-signup.html')

@views.route("/login")
def login():
    return render_template('login-signup.html')

@views.route("/order-complete")
def order_complete():
    #to show add to card info
    product_info = None
    if 'product-id' in session:
        ids = session['product-id']
        cursor.execute('SELECT * FROM products WHERE id IN %s', (ids,))
        product_info = cursor.fetchall()
    return render_template('order-complete.html', product_info=product_info)

@views.route("/blog")
def blog():
    #to show add to card info
    product_info = None
    if 'product-id' in session:
        ids = session['product-id']
        cursor.execute('SELECT * FROM products WHERE id IN %s', (ids,))
        product_info = cursor.fetchall()
    return render_template('blog.html', product_info=product_info)

@views.route("/secretespolicy")
def secretespolicy():
    #to show add to card info
    product_info = None
    if 'product-id' in session:
        ids = session['product-id']
        cursor.execute('SELECT * FROM products WHERE id IN %s', (ids,))
        product_info = cursor.fetchall()
    return render_template('secretespolicy.html', product_info=product_info)

@views.route("/terms_of_use")
def terms_of_use():
    #to show add to card info
    product_info = None
    if 'product-id' in session:
        ids = session['product-id']
        cursor.execute('SELECT * FROM products WHERE id IN %s', (ids,))
        product_info = cursor.fetchall()
    return render_template('terms-of-use.html', product_info=product_info)