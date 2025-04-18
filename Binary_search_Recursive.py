
def Binary_search_Recursive(lst, low, high, x):

    if low > high:

        return None

    else:

        mid = (low + high) // 2

        if lst[mid] == x:

            return mid

        elif lst[mid] > x:

            return Binary_search_Recursive(lst, low, mid - 1, x)

        else:

            return Binary_search_Recursive(lst, mid + 1, high, x)

def main():

    lst = [4, 12, 9, 2, 11, 15, 8, 3, 10, 1, 6, 13, 5, 7, 14]
    sorted_lst = sorted(lst)
    x = int(input('Enter your value for find: '))
    idx = Binary_search_Recursive(sorted_lst, 0, len(lst) - 1, x)
    print(f'Index of {x} = {idx}')

if __name__ == "__main__":
    main()