class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        hashtable = {}
        start = 0  

        for i in range(len(s)):
            if s[i] not in hashtable or hashtable[s[i]] < start:
                count = max(count, i - start + 1)
            else:
                start = hashtable[s[i]] + 1

            hashtable[s[i]] = i

        return count