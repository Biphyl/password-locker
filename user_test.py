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

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []


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


    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user
        objects to our user_list
        '''
        self.new_user.save_user()
        test_user = User("Instagram","biron_odhiambo","biron4745")

        test_user.save_user()
        self.assertEqual(len(User.user_list),2)


    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from our user list
        '''
        self.new_user.save_user()
        test_user = User("snapchat","bironotis","biron") # new user
        test_user.save_user()

        self.new_user.delete_user() # Deleting a user object
        self.assertEqual(len(User.user_list),1)

    def test_find_user_by_account_name(self):
        '''
        test to check if we can find user by account name and display information
        '''
        self.new_user.save_user()
        test_user = User("gmail","bironodhiambo00@gmail.com","biron 4745")
        test_user.save_user()
        found_user = User.find_by_account_name("gmail")
        self.assertEqual(found_user.login_username,test_user.login_username)




if __name__=='__main__':
    unittest.main()
