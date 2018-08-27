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

    def test_save_account(self): #second test
        '''
        test if the account is saved into the passwords list
        '''
        self.new_account.save_account() #saving the new account
        self.assertEqual(len(passwords.password_list),1)
 if __name__ ==  '__main__':
    unittest.main(
