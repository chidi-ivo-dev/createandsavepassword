import unittest
from password_locker import User

def setUp(self):
    '''
    Set up method to run before each test class
    '''
    self.new_user = User("Dan","Password","mungaiwaituika@gmail.com") #create a new user object

def test_init(self):
    '''

    :param self:
    :return:
    '''