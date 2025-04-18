
# register Function
def register():
    stored_value = open('database1.txt', 'r')

    d = []
    f = []

    for i in stored_value:
        a , b = i.split(',')
        b = b.strip()
        d.append(a)
        f.append(b)
    data = dict(zip(d, f))
    # print (data)

    username = input('Create Username : ')

    if username in d:
        print('Username already exists, try again')
        register()
    else:
        print('Username created successfully')

    password = input('Create Password : ')
    password_again = input('confirm Password : ')

    if password != password_again:
        print ('Password dose Not match, try again')
        register()
    else:
        if len(password) <= 6:
            print ('Password is too short, try again')
            register()
        else:
            stored_value = open('database1.txt', 'a')
            stored_value.write(username + ', ' + password+ '\n')
            print ('Registered Successfully')
    stored_value.close()

# # access Function
#
# def access() :
#     stored_value = open('database1.txt', 'r')
#     username = input('Enter your username: ')
#     password = input('Enter your password: ')
#
#     if not len(username or password) < 1 :
#         d = []
#         f = []
#
#         for i in stored_value:
#             a, b = i.split(',')
#             b = b.strip()
#             d.append(a)
#             f.append(b)
#         data = dict(zip(d, f))
#         try :
#             if data[username] :
#                 try :
#                     if password == data[username] :
#                         print('Access granted')
#                         print('Hi, ', username)
#                     else :
#                         print('Access denied')
#                         access()
#                 except :
#                     print('Access denied')
#                     access()
#             else :
#                 print('Username or Password does not exist')
#                 access()
#         except :
#             print('Access denied')
#             access()
#     stored_value.close()
#
# # Login or Signup Option
#
# def login_signup_option():
#     option = input('Login | Signup: ')
#
#     if option == 'Signup':
#         register()
#
#     elif option == 'Login':
#         access()
#
#     else:
#         print('Please enter a valid option')
#         login_signup_option()

