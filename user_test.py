import unittest # Importing unittest
from user import User # Importing the User class

class TestUser(unittest.TestCase):
    """
    Test class that defines test cases for the user class behaviours.

    Args:
         unittest.TestCase:TestCase that help in creating test cases
    """

    def setUp(self):
        """
        set up method to run before each test cases.
        """
        #
        self.new_user = User("facebook","biron odhiambo","biron 4745") # Create user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.account_name,"facebook")
        self.assertEqual(self.new_user.login_username,"biron odhiambo")
        self.assertEqual(self.new_user.user_password,"biron 4745")


    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into the user list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)



if __name__=='__main__':
    unittest.main()
