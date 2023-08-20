def longest_repeating_substring(s):
    n = len(s)
    longest_substr = ""

    for i in range(n):
        for j in range(i+1, n):
            length = 0
            while (j + length < n) and (s[i + length] == s[j + length]):
                length += 1
            if length > len(longest_substr):
                longest_substr = s[i:i+length]
            if s[i + length] != s[j + length]:
                return -1
                break
        

    

    return longest_substr
