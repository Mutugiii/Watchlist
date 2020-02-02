# Searches for templates in the directory named templates
from flask import render_template,request, redirect, url_for
# Imports
from . import main
from ..request import get_movies, get_movie, search_movie
from ..models import Review
from .forms import ReviewForm

# The views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    popular_movies = get_movies('popular')
    upcoming_movies = get_movies('upcoming')
    now_playing_movies = get_movies('now_playing')
    
    title = 'Home - Welcome to The best Movie Review Website Online'

    search_movie = request.args.get('movie_query')

    if search_movie:
        return redirect(url_for('.search',movie_name = search_movie))
    else:
        return render_template('index.html', title=title, popular=popular_movies, upcoming=upcoming_movies, now_playing=now_playing_movies)


@main.route('/movie/<int:id>')
def movie(id):
    '''
    View Movie page that returns movie details
    '''
    movie = get_movie(id)
    title = f'{movie.title}'
    reviews = Review.get_reviews(movie.id)
    return render_template('movie.html', title=title, movie=movie, reviews = reviews)


@main.route('/search/<movie_name>')
def search(movie_name):
    '''
    View movie search results
    '''
    movie_name_list = movie_name.split(" ")
    movie_name_format = "+".join(movie_name_list)
    searched_movie = search_movie(movie_name_format)
    # title = f'Search result for {movie_name}'
    return render_template('search.html', movies = searched_movie)


@main.route('/movie/review/new/<int:id>', methods = ['GET', 'POST'])
def new_review(id):
    form = ReviewForm()
    movie = get_movie(id)

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        new_review = Review(movie.id,title,movie.poster,review)
        new_review.save_review()
        return redirect(url_for('.movie', id = movie.id ))

    title = f'{movie.title} review' 
    return render_template('new_review.html', title = title, review_form = form, movie = movie)

