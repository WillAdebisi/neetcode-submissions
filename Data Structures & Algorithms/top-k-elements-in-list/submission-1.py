class Solution:
    from collections import defaultdict
    import heapq
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = defaultdict(int)
        m = float('-inf')
        for item in nums:
            ans[item] += 1
        ans = tuple(ans.items())
        ans1 = [(-1 * k,v) for v,k in ans]
        heapq.heapify(ans1)
        res = []
        for i in range(k):
            res.append(heapq.heappop(ans1)[1])
        return res

        
        
        
        
        
        

        
        