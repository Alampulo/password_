import unittest
from password import Password

    class TestPassword(unittest.TestCase):
    def setUp(self):
     self.new_user = User("first_name","last_name","special_key")

    def test_init(self):
       self.assertEqual(self.new_user.first_name,"buju")
       self.assertEqual(self.new_user.last_name,"bantom")
       self.assertEqual(self.new_user.special_key,"13039042")
  # test2
  if __name__ == '__main__':
    unittest.main()

        def test_save_password(self):

        self.new_password.save_password() # saving the new contact
        self.assertEqual(len(Password.password_list),1)

 if __name__ ==  '__main__':
    unittest.main(
