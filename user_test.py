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


if __name__=='__main__':
    unittest.main()
