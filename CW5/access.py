def access() :
    stored_value = open('database1.txt', 'r')
    username = input('Enter your username: ')
    password = input('Enter your password: ')

    if not len(username or password) < 1 :
        d = []
        f = []

        for i in stored_value:
            a, b = i.split(',')
            b = b.strip()
            d.append(a)
            f.append(b)
        data = dict(zip(d, f))
        try :
            if data[username] :
                try :
                    if password == data[username] :
                        print('Access granted')
                        print('Hi, ', username)
                    else :
                        print('Access denied')
                        access()
                except :
                    print('Access denied')
                    access()
            else :
                print('Username or Password does not exist')
                access()
        except :
            print('Access denied')
            access()

# access()