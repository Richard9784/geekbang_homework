class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fre_dict = collections.Counter(nums)
        heap = []
        res= []
        for i in fre_dict:
            heapq.heappush(heap,(-fre_dict[i], i))
        for j in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

