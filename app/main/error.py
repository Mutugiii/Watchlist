from flask import render_template
from . import main

@main.app_errorhandler(404)
def four_0_four(error):
    '''
    Handling 404 errors
    '''
    return render_template('404.html'),404
