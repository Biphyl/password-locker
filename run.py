from user import User

def create_user(account,username,password):
    '''
    Function to create a new user
    '''
    new_user = User(account,username,password)
    return new_user

def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()
