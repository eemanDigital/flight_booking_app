from flask import Flask

def create_app():
    '''initialises our app'''
    app = Flask(__name__)
    '''enable sucurity for the app'''
    app.config['SECRET_KEY'] = 'sllslsmandjdjgh dkkdfkdijds'

    '''register blueprints'''
    from .views import views
    from .booking import booking

    app.register_blueprint(views, url_prefix  ='/')
    app.register_blueprint(booking, url_prefix ='/')


    return app