class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(nums,path):
            if not nums and path not in res:
                res.append(path)
                for i in range(len(nums)):
                    backtrack(nums[:i]+nums[i+1:],path + [nums[i]])
        backtrack(nums,[])
        return res

#减枝操作
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.res = []
        check = [0 for i in range(len(nums))]

        self.backtrack(nums,[],check])
        return self.res
    
    def backtrack(self,nums,path,check):
        if len(path) == len(nums):
            self.res.append(path)
            return 
        for i in range(len(nums)):
            if check[i] == 1:
                continue
            if i > 0 and nums[i] == nums[i-1] and check[i-1] == 0:
                continue
            check[i] = 1
            self.backtrack(nums,path+[nums[i]],check)
            check[i] = 0

        
