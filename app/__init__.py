from flask import Flask
from flask_bootstrap import Bootstrap
#from flask_login import LoginManager


#login_manager = LoginManager()
#login_manager.session_protection = 'strong'
#login_manager.login_view = 'auth.login'


def create_app(config_name):


    app = Flask(__name__)

    app.secret_key = 'secret key'
    

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')


    # Initializing flask extensions
    Bootstrap(app)
    #login_manager.init_app(app)


    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)



    return app

