from flask import Blueprint,render_template, request, flash

booking = Blueprint('booking', __name__)

@booking.route('/flight', methods=['GET', 'POST'])
def flight():
    # '''retrive data from the form'''
    # data = request.form
    # print(data)
    return render_template('flight.html')

@booking.route('/home')
def home():
    return render_template('home.html')

@booking.route('/search')
def flight_search():
    return ('search.html')

@booking.route('/hotel')
def hotel():
    return render_template('hotel.html')

@booking.route('/login')
def login():
    return render_template('login.html')

@booking.route('/payment')
def payment():
    return render_template('payment.html')

@booking.route('/signup')
def signup():
    return render_template('signup.html')