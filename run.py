from user import User

def create_user(account_name,username,password):
    '''
    Function to create a new user
    '''
    new_user = User(account_name,username,password)
    return new_user

def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def find_user(account_name):
    '''
    Function that finds a user by username and returns the user
    '''
    return User.find_by_account_name(account_name)