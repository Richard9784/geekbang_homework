class Solution:
    def jump(self, nums: List[int]) -> int:
        cur_dis = 0
        far_dis = 0
        res = 0
        for i in range(len(nums) - 1):
            far_dis = max(nums[i] + i, far_dis)
            if i == cur_dis:
                cur_dis = far_dis
                res += 1
        return res
