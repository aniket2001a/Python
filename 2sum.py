def twoSum(nums, target):
    numMap = {}
    n = len(nums)
    for i in range(n):
        complement = target - nums[i]
        if complement in numMap:
            return [numMap[complement], i]
        numMap[nums[i]] = i
    return []

if __name__ == '__main__':
    nums = list(map(int, input().split()))  # Read input numbers
    target = int(input())  # Read target sum

    result = twoSum(nums, target)
    
    if result:
        print("Indices of two numbers:", result)
        print("Numbers:", nums[result[0]], nums[result[1]])
    else:
        print("No solution found.")