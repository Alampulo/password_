import unittest #import the unittest module
import pyperclip
from password import passwords #importing


class TestPasswords(unittest.TestCase):
    '''
    defines test cases for the password class behaviours
    Args:
        unittest.TestCase: helps in creating test cases
    '''
    def setUp(self):
        '''
        set up method to run before each test cases
        '''
        self.new_account = passwords("Account","Testname","TestPass")

    def tearDown(self):
        '''
        clean up after each test case has run
        '''
        passwords.password_list = []

    def test_init(self): #first test
        '''
        test if the object is initialized properly
        '''
        self.assertEqual(self.new_account.account_name,"Account")
        self.assertEqual(self.new_account.user_name,"Testname")
        self.assertEqual(self.new_account.password,"TestPass")

 if __name__ ==  '__main__':
    unittest.main(
