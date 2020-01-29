#importing Flask class
from flask import Flask  
from .config import DevConfig

# Initialize the application
app = Flask(__name__)

# Setting up Configuration
app.config.from_object(DevConfig)

# Importing views to allow us to create views
from app import views   

