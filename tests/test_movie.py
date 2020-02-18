import unittest
from app.models import Movie


class MovieTest(unittest.TestCase):
    '''
    Test class to test behaviour of test class
    Args:
        unittest.TestCase: Allows us to create test cases
    '''

    def setUp(self):
        '''
        So as to set up the tests correctly before they run
        '''
        self.new_movie = Movie(234, 'Python Must Be Crazy',
                               'A thrilling new Python Series', 'khsjha27hbs', 8.5, 129993)

    def test_instance(self):
        '''
        Test that it is an instance of a Movie class
        '''
        self.assertTrue(isinstance(self.new_movie, Movie))

    def test_init(self):
        '''
        Test if class is initialized correctly
        '''
        self.assertEqual(self.new_movie.id, 234)
        self.assertEqual(self.new_movie.title, 'Python Must Be Crazy')
        self.assertEqual(self.new_movie.overview,
                         'A thrilling new Python Series')
        self.assertEqual(self.new_movie.poster,
                         'https://image.tmdb.org/t/p/w500/khsjha27hbs')
        self.assertEqual(self.new_movie.vote_average, 8.5)
        self.assertEqual(self.new_movie.vote_count, 129993)
