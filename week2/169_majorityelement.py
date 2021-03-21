class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
        return max(dct.keys(), key=lambda x: dct[x])