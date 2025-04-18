def rem_advertise(username: str, title: str):

    with open('database2.txt', 'r') as file_in:
        lines = file_in.readlines()

    d = []
    f = []
    for i in lines:
        a, b = i.split(',')
        b = b.strip()
        d.append(a)
        f.append(b)


    found_username = False
    found_title = False
    found_access = False


    for i in range(len(lines)):
        a, b = lines[i].split(',')
        b = b.strip()


        if a == username:
            found_username = True


        if a == username and b == title:
            found_access = True
            found_title = True
            print(f"Deleting: {lines[i].strip()}")
            lines.pop(i)
            break


    if not found_username:
        print('Invalid Username')
    elif not found_title:
        print('Invalid Title')
    elif not found_access:
        print('Access denied')
    else:

        with open('database2.txt', 'w') as file_out:
            file_out.writelines(lines)
        print('Removed successfully')


delet_username = input('Please enter your username: ')
delet_title = input('Please enter your title: ')
rem_advertise(delet_username, delet_title)
