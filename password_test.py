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

   def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
   self.assertEqual(self.new_user.first_name,"buju")
   self.assertEqual(self.new_user.last_name,"bantom")
   self.assertEqual(self.new_user.special_key,"13039042")


  if __name__ == '__main__':
    unittest.main()
