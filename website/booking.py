from flask import Blueprint,render_template, request, flash

booking = Blueprint('auth', __name__)

@booking.route('/login', methods=['GET', 'POST'])
def login():
    # '''retrive data from the form'''
    # data = request.form
    # print(data)
    return render_template('login.html')

@booking.route('/logout')
def logout():
    return '<p>Logout</p>'