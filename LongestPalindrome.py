def is_palindrome(s):
    return s == s[::-1]

def longest_palindrome(strings):
    longest = ""
    for s in strings:
        if is_palindrome(s) and len(s) > len(longest):
            longest = s
    return longest

if __name__ == '__main__':
    string_list = input("Enter a list of strings separated by spaces: ").split()
    
    longest = longest_palindrome(string_list)
    
    if longest:
        print("Longest palindrome:", longest)
    else:
        print("No palindrome found.")
