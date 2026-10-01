from heapq import heappush, nlargest, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = []
        freq = {}
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 0
        
        for f in freq:
            heappush(h,(freq[f],f))
            if len(h) > k:
                heappop(h)
        
        r = []
        for t in h:
            r.append(t[1])

        return r