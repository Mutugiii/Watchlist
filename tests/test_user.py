import unittest
from app.models import User

class UserModelTest(unittest.TestCase):
    '''
    Class to test the User Model Class/able
    '''
    def setUp(self):
        '''
        Setup before each test case
        '''
        self.new_user = User(password = 'banana')
    
    def test_password_setter(self):
        '''
        Test case that password always contains a value when being hashed
        '''
        self.assertTrue(self.new_user.pass_secure is not None)

    def test_no_access_password(self):
        '''
        Confirm app raises attribute Error on access password property
        '''
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        '''
        Ensure password hash can be verified when we pass in correct password
        '''
        self.assertTrue(self.new_user.verify_password('banana'))


