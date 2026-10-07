class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        biggest = max(nums)
        target = sum(range(biggest+1))
        actual = sum(nums)
        res = target-actual
        if res in nums:
            return biggest+1
        else:
            return res