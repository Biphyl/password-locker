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


        