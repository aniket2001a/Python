def max_product_of_two(nums):
    if len(nums) < 2:
        return None
    
    max1, max2 = float('-inf'), float('-inf')
    min1, min2 = float('inf'), float('inf')
    
    for num in nums:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
        
        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num
    
    return max(max1 * max2, min1 * min2)

if __name__ == '__main__':
    nums = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
    max_prod = max_product_of_two(nums)
    
    if max_prod is not None:
        print("Maximum product of two integers:", max_prod)
    else:
        print("The list should contain at least two integers.")