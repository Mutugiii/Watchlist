from .models import Movie
import urllib.request, json

# Getting api key & base url
api_key = None
base_url = None

def configure_request(app):
    global api_key, base_url
    api_key = app.config['MOVIE_API_KEY']
    base_url = app.config['MOVIE_API_BASE_URL']

def process_results(movies_dict):
    '''
    Function to process the dictionary received from the get_movies call; Convert res to movie list from dict && sorts data
    Args:
        movies_dict: A dictionary list of movies
    Returns:
        A list of movies
    '''
    movies_list = []
    for movie in movies_dict:
        id = movie.get('id')
        title = movie.get('original_title')
        overview = movie.get('overview')
        poster = movie.get('poster_path')
        vote_average = movie.get('vote_average')
        vote_count = movie.get('vote_count')

        if poster:
            movie_object = Movie(id,title,overview,poster,vote_average,vote_count)
            movies_list.append(movie_object)

    return movies_list


def get_movies(category):
    '''
    Function to get the movies
    '''
    #get_movies_response = json.loads(urllib.request.urlopen(base_url.format(category,api_key)).read())
    movies_url = base_url.format(category,api_key)

    with urllib.request.urlopen(movies_url) as url:
        get_movies_data = url.read()
        get_movies_response = json.loads(get_movies_data)

        movies_results = None
        
        if get_movies_response['results']:
             movies_results_dict = get_movies_response['results']
             movies_results = process_results(movies_results_dict)
    return movies_results


def get_movie(id):
    '''
    Function to get a specific movie
    '''
    movie_details = json.loads(urllib.request.urlopen(base_url.format(id,api_key)).read())

    movie_object = None
    if movie_details:
        id = movie_details.get('id')
        title = movie_details.get('original_title')
        overview = movie_details.get('overview')
        poster = movie_details.get('poster_path')
        vote_average = movie_details.get('vote_average')
        vote_count = movie_details.get('vote_count')

        movie_object = Movie(id,title,overview,poster,vote_average,vote_count)
    return movie_object

def search_movie(name):
    '''
    Function to search for a specific movie by name
    '''
    search_movie_url = 'https://api.themoviedb.org/3/search/movie?api_key={}&query={}'.format(api_key,name)
    movie_search = json.loads(urllib.request.urlopen(search_movie_url).read())

    name_results = None
    if movie_search['results']:
        name_results = process_results(movie_search['results'])
    return name_results
