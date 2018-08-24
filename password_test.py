import unittest
from Password import Password

class TestPassword(unittest.TestCase):
     '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

  def setUp(self):
     '''
     Set up method to run before each test cases.
     '''
      self.new_user = User("first_name","last_name","special_key")
