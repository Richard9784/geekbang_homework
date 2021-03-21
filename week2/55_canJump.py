class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums == [0]: return True
        max_i = 0
        end = len(nums) - 1
        for i, jump in enumerate(nums):
            if max_i >= i and i+jump>max_i:
                max_i = i + jump
                if max_i >= end:
                    return True
        return False