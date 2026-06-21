class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output=[1]*len(nums)

        totalbefore=1
        for i in range(len(nums)):
            output[i]=totalbefore
            totalbefore*=nums[i]

        totalafter=1
        for i in range(len(nums)-1,-1,-1):
            output[i]*=totalafter
            totalafter*=nums[i]

        return output

