class Solution:
    def isValid(self, s: str) -> bool:
        if not s: return True
        if "()" in s:
            return self.isValid(s[:s.index("()")]+s[s.index("()")+2:])
        if "[]" in s:
            return self.isValid(s[:s.index("[]")]+s[s.index("[]")+2:])
        if "{}" in s:
            return self.isValid(s[:s.index("{}")]+s[s.index("{}")+2:])
        return False
        