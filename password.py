import random
import pyperclip
class user:
    '''
    class that generates new instances of user account
    '''
    user_list = []
    def __init__(self,name,pwd):
        self.name = name
        self.pwd = pwd

    def save_user(self):
        '''
        save user details into user_list
        '''
        user.user_list.append(self)

    def generate_password(self):
        '''
        generate new password
        '''
        chars = '1234567890abcdefghijklmnop?/@-' #characters to choose from
        length = int(input("Enter the length of password you want: "))
        pwd = ''
        for c in range(length):
            pwd += random.choice(chars) #generate random password
        print (pwd)
class passwords:
    '''
    class that generates new instances of passwords
    '''
    password_list = []
    def __init__(self,account_name,user_name,password):
        '''
        init method helps us define properties for our objects
        '''
        self.account_name = account_name
        self.user_name = user_name
        self.password = password

    def save_account(self):
        '''
        save contact object into password_list
        '''
        passwords.password_list.append(self)

    def delete_account(self):
        '''
        delete account
        '''
        passwords.password_list.remove(self)
