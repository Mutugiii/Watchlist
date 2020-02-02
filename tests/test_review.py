import unittest
from app.models import Review

class ReviewTest(unittest.TestCase):
    '''
    Class to test the Review class
    '''

    def setUp(self):
        '''
        Set up before each test case
        '''

        self.new_review = Review(454,"Hello movies", "https://img.com","user review")

    def tearDown(self):
        '''
        Clean up after every test case
        '''
        self.new_review = Review(0,"", "","")
    
    def test_instance(self):
        '''
        Test that it is an instance of a Movie class
        '''
        self.assertTrue(isinstance(self.new_review,Review))

    def test_init(self):
        '''
        Test if class is initialized correctly
        '''
        self.assertEqual(self.new_movie.id,454)
        self.assertEqual(self.new_movie.title,'Hello movies')
        self.assertEqual(self.new_movie.imageurl,"https://img.com")
        self.assertEqual(self.new_movie.review,"user review")


