class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = {}
        res = []
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        sd = sorted(d.items(), key=lambda item: item[1], reverse=True)
        for i in range(k):
            res.append(sd[i][0])
        return res

