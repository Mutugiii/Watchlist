#importing Flask class
from flask import Flask  
from .config import DevConfig

# Initialize the application
app = Flask(__name__, instance_relative_config = True)

# Setting up Configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

# Importing views to allow us to create views
from app import views   

