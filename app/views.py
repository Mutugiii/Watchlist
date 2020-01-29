# Searches for templates in the directory named templates
from flask import render_template 
# Import app instance from app folder
from app import app 

# The views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    titlea = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', titled = titlea)

@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    '''
    View Movie page that returns movie details
    '''
    return render_template('movie.html', id = movie_id)
