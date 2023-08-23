def longest_valid_parentheses(s):
    stack = [-1]  # Initialize the stack with -1
    max_length = 0
    
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if len(stack) == 0:
                stack.append(i)
            else:
                max_length = max(max_length, i - stack[-1])
    
    return max_length

if __name__ == '__main__':
    input_string = input("Enter a string containing parentheses: ")
    length = longest_valid_parentheses(input_string)
    print("Length of the longest valid parentheses substring:", length)
