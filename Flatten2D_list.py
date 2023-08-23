def flatten_2d_list(lst_2d):
    flattened = []
    for sublist in lst_2d:
        for item in sublist:
            flattened.append(item)
    return flattened

if __name__ == '__main__':
    rows = int(input("Enter the number of rows in the 2D list: "))
    cols = int(input("Enter the number of columns in the 2D list: "))
    
    lst_2d = []
    for _ in range(rows):
        row = list(map(int, input(f"Enter {cols} numbers separated by spaces: ").split()))
        lst_2d.append(row)
    
    flattened_list = flatten_2d_list(lst_2d)
    print("Flattened list:", flattened_list)


# If cols are different sizes
'''
if __name__ == '__main__':
    rows = int(input("Enter the number of rows in the 2D list: "))
    
    lst_2d = []
    for _ in range(rows):
        row = list(map(int, input("Enter numbers separated by spaces for this row: ").split()))
        lst_2d.append(row)
    
    flattened_list = flatten_2d_list(lst_2d)
    print("Flattened list:", flattened_list)

'''