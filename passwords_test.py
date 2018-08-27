import unittest
import pyperclip
from password import passwords

class TestPasswords(unittest.TestCase):

    def setUp(self):

        self.new_account = passwords("Account","Testname","TestPass")

    def tearDown(self):

        passwords.password_list = []

    def test_init(self):

        self.assertEqual(self.new_account.account_name,"Account")
        self.assertEqual(self.new_account.user_name,"Testname")
        self.assertEqual(self.new_account.password,"TestPass")

    def test_save_account(self):
        self.new_account.save_account()
        self.assertEqual(len(passwords.password_list),1)

    def test_save_multiple_accounts(self):

        self.new_account.save_account()
        test_account = passwords("Account","Testname","TestPass")
        test_account.save_account()
        self.assertEqual(len(passwords.password_list),2)

    def test_delete_passwords(self):
        self.new_account.save_account()
        test_account = passwords("Account","Testname","TestPass")
        test_account.save_account()
        self.new_account.delete_account()
        self.assertEqual(len(passwords.password_list),1)

    def test_find_account_by_account_name(self):
        self.new_account.save_account()
        test_account = passwords("Account","Testname","TestPass")
        test_account.save_account()
        found_account = passwords.find_by_account("Account")
        self.assertEqual(found_account.user_name, test_account.user_name)

    def test_account_exists(self):
        self.new_account.save_account()
        test_account = passwords("Account","Testname","TestPass")
        test_account.save_account()
        account_exists = passwords.account_exists("Account")
        self.assertTrue(account_exists)

    def test_display_accounts(self): 
        self.assertEqual(passwords.display_accounts(),passwords.password_list)

if __name__ == '__main__':
    unittest.main()
