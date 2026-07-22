class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        longest = 0
        l=0
        for r in range(len(s)):
            counts[s[r]] = counts.get(s[r],0) + 1

            while((r-l+1) - max(counts.values()) > k):
                counts[s[l]] -= 1
                l+=1
            
            longest = max(longest, r-l + 1)
        return longest
