import unittest
from .models import review

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
    
    #def test_init(self):
        #self.assertEqual()

