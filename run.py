import random
from password import passwords
from password import user

def create_user(name,pwd):

    new_user = user(name,pwd)
    return new_user
def save_user(user):

    user.save_user()
def generate_password(user):

    user.generate_password()


def create_account(account_name, user_name, password):

    new_account = passwords(account_name, user_name, password)
    return new_account

def save_account(account):

    account.save_account()

def del_account(account):

    account.delete_account()

def find_account(account_name):

    return passwords.find_by_account(account_name)

def check_existing_account(account_name):

    return passwords.account_exists(account_name)

def display_accounts():

    return passwords.display_accounts()


def main():
    print("**************** Password Locker World Welcome*************")
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
        chars = 'abcdefGHIJKlmn1256784903-@!&#.'
        length = int(input("Enter the length of password you want: "))
        pwdinput = ''
        for c in range(length):
            pwdinput += random.choice(chars)
        print (pwdinput)
        print(f"{username} your password is {pwdinput}")

    elif (pwd_click == 'c'):
        print("Input password: ")
        pwdinput = input()
        print(f"{username} your password is {pwdinput}")

        print("\n"*2)

    save_user(create_user(username,pwdinput))

    print('\n' * 2)
    print (f"New user {username} created.")
    print('\n' * 2)

    print("To continue reenter yuh details")
    print("*"*78)
    print("Enter yuh username : ")
    name = input()
    print("Enter yur password: ")
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

                save_account(create_account(account_name,user_name,password))

                print('\n' * 1)
                print (f"New account {account_name} created.")
                print('\n' * 1)

            elif short_code == 'd':
                if display_accounts():
                    print("Here are your accounts: ")
                    print('\n')
                    for account in display_accounts():
                        print(f"{account.account_name}  {account.user_name}  {account.password}")
                        print('\n')
                else:
                    print('\n')
                    print("Sorry...You dont have any saved acccounts")
                    print('\n')

            elif short_code == 'f':
                print("Enter search name: ")
                search_account_name = input()
                if check_existing_account(search_account_name):
                    search_account = find_account(search_account_name)
                    print(f"{search_account.account_name}")
                    print('-' * 20)
                    print(f"User Name...................{search_account.user_name}")
                    print(f"Password...................{search_account.password}")

                else:
                    print("Account does not exist")

            elif short_code == 'ex':
                print("Thanks")
                break
            else:
                print("Sorry YOh shit input!Try short codes")


if __name__ == '__main__':
    main()
