# importing Flask class
from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_mail import Mail
from flask_simplemde import SimpleMDE

# Initalizations
bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
photos = UploadSet('photos', IMAGES)
mail = Mail()
simple = SimpleMDE()

# App factory function


def create_app(config_name):
    # Initialize the application
    app = Flask(__name__)

    # Creating app Configuration
    app.config.from_object(config_options[config_name])

    # Initialize flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    configure_uploads(app, photos)
    mail.init_app(app)
    simple.init_app(app)

    # Registering blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # Setting up config
    from .request import configure_request
    configure_request(app)

    return app
