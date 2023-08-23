def longest_substring_of_char(s, char):
    max_length = 0
    current_length = 0

    for c in s:
        if c == char:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 0

    return max_length

if __name__ == '__main__':
    input_string = input("Enter a string: ")
    target_char = input("Enter the character to find the longest substring of: ")

    length = longest_substring_of_char(input_string, target_char)
    print(f"Longest substring of '{target_char}' in the string:", length)
