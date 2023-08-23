def find_largest_integer(matrix):
    if not matrix:
        return None
    
    max_int = float('-inf')
    
    for row in matrix:
        for num in row:
            if num > max_int:
                max_int = num
    
    return max_int

if __name__ == '__main__':
    rows = int(input("Enter the number of rows in the matrix: "))
    cols = int(input("Enter the number of columns in the matrix: "))
    
    matrix = []
    for _ in range(rows):
        row = list(map(int, input(f"Enter {cols} numbers separated by spaces: ").split()))
        matrix.append(row)
    
    largest_int = find_largest_integer(matrix)
    
    if largest_int is not None:
        print("Largest integer in the matrix:", largest_int)
    else:
        print("The matrix should contain at least one element.")
