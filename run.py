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




if __name__ == '__main__':
    main()
