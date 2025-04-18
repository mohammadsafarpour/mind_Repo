from register import register
from access import access

def login_signup_option() :

    option = input('Login | Signup: ')

    option = option.lower()
    option = option.capitalize()

    if option == 'Signup' :
        register()

    elif option == 'Login' :
        access()

    else :
        print('Please enter a valid option')
        login_signup_option()

login_signup_option()