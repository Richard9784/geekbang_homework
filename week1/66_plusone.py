class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = 0
        for i in digits:
            n = n*10 +i
        return [int(x) for x in str(n+1)]