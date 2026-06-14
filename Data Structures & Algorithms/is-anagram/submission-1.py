class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        for i in range(len(s)):
            if s[0] in t:
                t = t[:t.find(s[0])]+t[t.find(s[0])+1:]
                s = s[1:]
            if len(s)==0:
                return True
        return False
