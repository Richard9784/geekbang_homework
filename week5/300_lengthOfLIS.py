class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:return 0
        N = len(nums)
        dp = [1] * N
        for i in range(N):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp = max(dp[i],dp[j]+1)
        return max(dp)
        