class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        for char in s:
            if char in t:
                t = t.replace(char,"",1)
        if len(t)==0: return True
        return False
