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
