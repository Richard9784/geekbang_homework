class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        n1 = len(arr1)
        n2 = len(arr2)
        res = []
        arr1.sort()
        count = collections.Counter(arr1)
        for num in arr2:
            res.extend([num]*count[num])
        for num in arr1:
            if num not in arr2:
                res.append(num)
        return res

