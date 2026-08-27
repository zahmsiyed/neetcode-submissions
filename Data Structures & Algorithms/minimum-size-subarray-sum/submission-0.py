class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minlen = float("inf")
        l = 0
        total = 0
        for r in range(len(nums)):
            total += nums[r]
            while total>=target:
                minlen = min(minlen, r-l+1)
                total -= nums[l]
                l+=1
        if minlen==float("inf"): return 0 
        else: return minlen
