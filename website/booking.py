from flask import Blueprint,render_template, request, flash

booking = Blueprint('booking', __name__)

@booking.route('/flights', methods=['GET', 'POST'])
def flights():
    # '''retrive data from the form'''
    # data = request.form
    # print(data)
    return render_template('flights.html')

@booking.route('/home')
def home():
    return render_template('home.html')

@booking.route('/search')
def flight_search():
    return ('search.html')

@booking.route('/bookings')
def bookings():
    return render_template('bookings.html')

@booking.route('/login')
def login():
    return render_template('login.html')

@booking.route('/payment')
def payment():
    return render_template('payment.html')

@booking.route('/signup')
def signup():
    return render_template('signup.html')