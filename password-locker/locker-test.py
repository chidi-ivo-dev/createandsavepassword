import unittest # Importing the unittest module
import pyperclip
from locker import User # Importing the User class

def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_User = User("Dan","Password","Mungaiwaituika@gmail.com") # create user object


def test_init(self):
    '''
    test_init test case to test if the object is initialized properly
    '''

    self.assertEqual(self.new_User.user_name,"Dan")
    self.assertEqual(self.new_User.password,"Password")
    self.assertEqual(self.new_User.email,"Mungaiwaituika@gmail.com")


if __name__ == '__main__':
    unittest.main()