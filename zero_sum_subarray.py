def count_zero_sum_subarrays(arr):
    sum_count = {}  # Dictionary to store cumulative sum frequencies
    cumulative_sum = 0  # Initialize cumulative sum
    count = 0  # Initialize count of zero sum subarrays

    for num in arr:
        cumulative_sum += num
        
        # If the cumulative sum is 0, increment the count
        if cumulative_sum == 0:
            count += 1
        
        # Check if the cumulative sum has been seen before
        if cumulative_sum in sum_count:
            count += sum_count[cumulative_sum]
        
        # Update the cumulative sum frequency
        if cumulative_sum in sum_count:
            sum_count[cumulative_sum] += 1
        else:
            sum_count[cumulative_sum] = 1
    
    return count

if __name__ == '__main__':
    arr = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
    zero_sum_count = count_zero_sum_subarrays(arr)
    print("Number of subarrays with sum 0:", zero_sum_count)
