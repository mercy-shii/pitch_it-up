from flask import Flask
from flask_bootstrap import Bootstrap

def create_app(config_name):


    app = Flask(__name__)

    app.secret_key = 'secret key'
    

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')


    # Initializing flask extensions
    Bootstrap(app)


    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)



    return app

