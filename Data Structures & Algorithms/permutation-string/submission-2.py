class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Counts = {}
        for char in s1:
            s1Counts[char] = s1Counts.get(char, 0)+1
        l=0;
        r=len(s1)
        while (r<=len(s2)):
            s2Counts = {}
            for char in s2[l:r]:
                s2Counts[char] = s2Counts.get(char,0)+1
            if s1Counts==s2Counts:
                return True
            l+=1
            r+=1
        return False


