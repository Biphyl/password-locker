class User:
    """ 
    Class that generate new instance of user.
    """
    def __init__(self, account_name, login_username, user_password):
        '''
        Initializing the variables
        '''
        self.account_name = account_name
        self.login_username = login_username
        self.user_password = user_password