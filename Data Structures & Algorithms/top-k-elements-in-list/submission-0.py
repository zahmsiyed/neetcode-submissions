class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = {}
        uniquenums=[]
       
        for num in nums:
            if num not in uniquenums:
                uniquenums.append(num)
        
        for uniquenum in uniquenums:
            count = 0
            for num in nums:
                if num==uniquenum:
                    count+=1
            counts[uniquenum] = count

        sorteddict = sorted(counts, key=counts.get, reverse=True)
        return sorteddict[:k]