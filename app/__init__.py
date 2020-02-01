#importing Flask class
from flask import Flask
from flask_bootstrap import Bootstrap
from .config import DevConfig

# Initialize the application
app = Flask(__name__, instance_relative_config = True)

# Setting up Configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

# Initalize bootstrap
bootstrap = Bootstrap(app)

# Importing views to allow us to create views & error for error handling
from app import views
from app import error

