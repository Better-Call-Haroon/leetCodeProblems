class Solution:
    def isPalindrome(self, s: str) -> bool:
          s = re.sub(r'[^a-zA-Z0-9]', '', s)
          s=s.lower()
          if len(s)==1:
            return True
          elif len(s)==2:
            return s[0] == s[1]
          else:
            if s==s[::-1]:
                return True
            else:
                return False

        