import random
import pyperclip
class user:

    user_list = []
    def __init__(self,name,pwd):
        self.name = name
        self.pwd = pwd

    def save_user(self):

        user.user_list.append(self)

    def generate_password(self):

        chars = '1234567890abcdefghijklmnop?/@-'
        length = int(input("Enter the length of password you want: "))
        pwd = ''
        for c in range(length):
            pwd += random.choice(chars)
        print (pwd)
class passwords:

    password_list = []
    def __init__(self,account_name,user_name,password):

        self.account_name = account_name
        self.user_name = user_name
        self.password = password

    def save_account(self):

        passwords.password_list.append(self)

    def delete_account(self):

        passwords.password_list.remove(self)

    @classmethod
    def find_by_account(cls,account_name):

        for account in cls.password_list:
            if account.account_name == account_name:
                return account

    @classmethod
    def account_exists(cls, account_name):

        for account in cls.password_list:
            if account.account_name == account_name:
                return True
        return False


    @classmethod
    def display_accounts(cls):
        
        return cls.password_list
