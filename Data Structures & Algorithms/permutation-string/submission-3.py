class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1Counts = {}
        windowCounts = {}

        for char in s1:
            s1Counts[char] = s1Counts.get(char, 0) + 1

        l = 0
        r = len(s1)

        for char in s2[l:r]:
            windowCounts[char] = windowCounts.get(char, 0)+1
        if s1Counts==windowCounts: return True

        while r < len(s2):
            oldChar = s2[l]
            newChar = s2[r]
            windowCounts[oldChar] = windowCounts[oldChar] - 1
            if windowCounts[oldChar] == 0: windowCounts.pop(oldChar)
            windowCounts[newChar] = windowCounts.get(newChar, 0)+1
            
            if s1Counts == windowCounts:
                return True
            l += 1
            r += 1
        return False
