class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones: return 0
        
        stones = [-n for n in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)
            if x==y:
                continue
            elif x<y:
                y = y-x
                heapq.heappush(stones, -y)
            else: #y<x
                x = x-y
                heapq.heappush(stones, -x)
        
        if not stones: return 0
        return -stones[0]