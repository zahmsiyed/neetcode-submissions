class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        result = []
        h = nums
        heapq.heapify(h)
        for _ in range(len(nums)):
            result.append(heapq.heappop(h))
        return result