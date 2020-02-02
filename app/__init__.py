#importing Flask class
from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

# Initalize bootstrap
bootstrap = Bootstrap()

# App factory function
def create_app(config_name):
    # Initialize the application
    app = Flask(__name__)
    
    # Creating app Configuration
    app.config.from_object(config_options[config_name])

    # Initialize flask extensions
    bootstrap.init_app(app)
    
    # Registering a blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Setting up config
    from .request import configure_request
    configure_request(app)

    return app

