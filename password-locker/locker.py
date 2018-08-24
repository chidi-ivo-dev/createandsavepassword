import random
import pyperclip
def all():
    print('Already have an account? (y/n)')
    answer =input().lower()
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

        handle = open("details.txt","a")

        handle.write(username)
        handle.write(" ")
        handle.write("password")
        handle.write(" ")
        handle.write("email")
        handle.write("/n")

        handle.close()
        print("Account you just made has been created successfully")