def rotate_list_clockwise(lst, n):
    n = n % len(lst)  # Normalize n to the range of list length
    return lst[-n:] + lst[:-n]

# IF VOID FUNCTION IS GIVEN
def rotate(lst, k):
    k = k%len(lst)

    lst[:] = lst[::-1]
    lst[:k] = lst[:k][::-1]
    lst[k:] = lst[k:][::-1]


if __name__ == '__main__':
    lst = input("Enter a list of elements separated by spaces: ").split()
    n = int(input("Enter the number of steps to rotate clockwise: "))
    
    # rotated_list = rotate_list_clockwise(lst, n)
    
    # print("Rotated list:", rotated_list)

    rotate(lst, n)
    print(lst)


    # li = []
    # for i in range (len(rotated_list)):
    #     li.append(int(rotated_list[i]))
        
    # print(li)
