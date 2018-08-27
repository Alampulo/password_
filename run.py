#!/usr/bin/env python3.6
import random
from password import passwords
from password import user
#methods for user
def create_user(name,pwd):
    '''
    function to create new user
    '''
    new_user = user(name,pwd)
    return new_user
def save_user(user):
    '''
    function to save user details
    '''
    user.save_user()
def generate_password(user):
    '''
    function to generate password
    '''
    user.generate_password()

#methods for passwords
def create_account(account_name, user_name, password):
    '''
    function to create new account
    '''
    new_account = passwords(account_name, user_name, password)
    return new_account

def save_account(account):
    '''
    function to save account
    '''
    account.save_account()

def del_account(account):
    '''
    function to delete account
    '''
    account.delete_account()
def find_account(account_name):
    '''
    function to find account by account name
    '''
    return passwords.find_by_account(account_name)
def check_existing_account(account_name):
    '''
    function that checks if account exists
    '''
    return passwords.account_exists(account_name)
    def display_accounts():
    '''
    function that returns saved accounts
    '''
    return passwords.display_accounts()


def main():
    print("****************karribu sana kwa Password Locker*************")
    print("\n")
    print("Enter your name: ")
    username = input()
    print("*"*78)
    print(f"Hello {username}.\nEnter a password or automatically generate password by system?")
    print('''
        Press:
                    g- automatically generate new password
                    c- create your own password
          ''')
          pwd_click = input()
    if (pwd_click  == 'g'):
        chars = 'abcdefGHIJKlmn1256784903-@!&#.' #characters to choose from
        length = int(input("Enter the length of password you want: "))
        pwdinput = ''
        for c in range(length):
            pwdinput += random.choice(chars) #generate random password
        print (pwdinput)
        print(f"{username} your password is {pwdinput}")

        elif (pwd_click == 'c'):
        print("Input password: ")
        pwdinput = input()
        print(f"{username} your password is {pwdinput}")

        print("\n"*2)

    save_user(create_user(username,pwdinput))
    #create and save user passwords
    print('\n' * 2)
    print (f"New user {username} created.")
    print('\n' * 2)

    print("To continue reenter your details")
    print("*"*78)
    print("Enter your username : ")
    name = input()
    print("Enter your password: ")
    pwd = input()
    if (name == username and pwd == pwdinput):
        print('\n')
        while True:
            print('''Use these short codes:
                  c - create new account
                  d - display accounts
                  f - find accounts
                  ex - exit accounts
                  ''')
            short_code = input().lower()
            if short_code == 'c':
                print("*************Create new account***********")
                print("-"*80)
                print("Account Name: ")
                account_name = input()
                print("User Name: ")
                user_name = input()
                print("Password for account: ")
                password = input()
            



if __name__ == '__main__':
    main()
