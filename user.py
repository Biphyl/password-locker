class User:
    """ 
    Class that generate new instance of user.
    """
    user_list = [] #Empty user list

    def __init__(self, account_name, login_username, user_password):
        '''
        Initializing the variables
        '''
        self.account_name = account_name
        self.login_username = login_username
        self.user_password = user_password

    def save_user(self):
        '''
        save_user method saves user object into user_list
        '''
        User.user_list.append(self)

    def delete_user(self):
        '''
        delete_user method dleltes a saved user from the user_list
        '''
        User.user_list.remove(self)

    @classmethod
    def find_by_account_name(cls,any):
        '''
        Method that taked in any value and returns the user that matches the value

        Args:
            any: Value of the account_name to search for
        Returns : 
            user that matches the account_name
        ''' 

        for user in cls.user_list:
            if user.account_name == any:
                return user