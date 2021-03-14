class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        N = len(nums)
        j = 0
        for i in range(N):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
