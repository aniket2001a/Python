def longestPalindrome(self, S):
        # code here
        s_prime = '#' + '#'.join(S) + '#'
        n = len(s_prime)
        palindrome_radii = [0] * n
        center = radius = 0
        
        for i in range(n):
            mirror = 2 * center - i

            if i < radius:
                palindrome_radii[i] = min(radius - i, palindrome_radii[mirror])

            while (i + 1 + palindrome_radii[i] < n and 
                   i - 1 - palindrome_radii[i] >= 0 and
                   s_prime[i + 1 + palindrome_radii[i]] == s_prime[i - 1 - palindrome_radii[i]]):
                palindrome_radii[i] += 1

            if i + palindrome_radii[i] > radius:
                center = i
                radius = i + palindrome_radii[i]

        max_length = max(palindrome_radii)
        center_index = palindrome_radii.index(max_length)
        start_index = (center_index - max_length) // 2
        longest_palindrome = S[start_index: start_index + max_length]
        
        # print(len(longest_palindrome))

        return longest_palindrome