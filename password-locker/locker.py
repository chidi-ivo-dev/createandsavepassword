import random
import pyperclip


def all():
    print('Already have an account? (y/n)')
    answer = input().lower()
    if answer == 'n':
        print("enter your name:")
        username = input()
        print("/n")
        print("Enter a password")
        password = input()
        print("/n")
        print("Enter your email")
        email = input()
        print('/n')

        handle = open("details.txt", "a")

        handle.write(username)
        handle.write(" ")
        handle.write("password")
        handle.write(" ")
        handle.write("email")
        handle.write("/n")

        handle.close()
        print("Account you just made has been created successfully /n Would you like to do more with password "
              "locker?(y/n)")
        responce = input().lower()
        if responce == 'y':
            generate_account()

        else:
            print("be sure to come back if you'd like to save a password, Have a good day!")

    elif answer == 'y':
        login()


def generate_account():
    print("Which account would you like to generate an account for?")
    account_to_be_saved = input()
    print("Enter 'auto'- for an auto-generated password or 'type'- to type in your own password")
    choice = input()
    if choice == 'auto':
        reversed_account_name = account_to_be_saved[::-1]
        r = str(random.randint(0, 20))
        password = reversed_account_name + r
        print(f"your new password is {password}")
        handle.write(account_to_be_saved)
        handle.write(" ")
        handle.write(password)
        handle.write("")

        handle.close()

        print(f"the password to your new account {account_to_be_saved} account is {password} and has been saved to "
              f"your clipboard has been saved and can be copied to the clipboard, you couls even apste it here in the "
              f"terminal. try it, (ctr + shift + v)")
        pyperclip.copy(password)

    else:
        print("type in your password")
        password = input()
        pyperclip.copy(password)
        print(f"the password to your new account {account_to_be_saved} account is {password} and has been saved to "
              f"your clipboard has been saved and can be copied to the clipboard, you couls even paste it here in the "
              f"terminal. try it, (ctr + shift + v)")
