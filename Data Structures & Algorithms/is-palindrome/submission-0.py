class Solution:
    def isPalindrome(self, s: str) -> bool:
        nospaces = ""
        for i in range(len(s)):
            if s[i].isalnum(): 
                nospaces += s[i].lower()
        return nospaces == nospaces[::-1]