import random

class user:

    user_list = []


    def __init__(self, username, email, password):

        self.username = username
        self.password = password

    def save_user(self):
        
        User.user_list.append(self)

def generate_password(self, account_password):
        print("How many digits would you like 4 ur  password?")
        y = input()
        for x in range (y):
            account_password = random.randint(1, 10)
            print(account_password)
