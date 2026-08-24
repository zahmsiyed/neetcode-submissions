class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        count = 0
        biggest = 0
        for num in nums:
            dic[num] = dic.get(num,0)+1
            if count < dic[num]:
                biggest = num
                count = dic[num]
        return biggest