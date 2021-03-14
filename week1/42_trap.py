#暴力解法，一格一格考虑
class Solution:
    def trap(self,height):
        ans = 0
        n = len(height)
        for i in range(n):
            max_left, max_right = 0, 0
            for j in range(0,i):
                max_left = max(max_left,height[j])
            for j in range(i,n):
                max_right = max(max_right,height[j])
            ans += min(max_right,max_left) - height[i]
        return ans

#双指针
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:return 0
        n = len(height)
        left,right = 0, n-1
        maxleft,maxright = height[0], height[n-1]
        ans = 0
        while left < right:
            maxleft = max(maxleft,height[left])
            maxright = max(maxright,height[right])
            if maxleft < maxright:
                ans += maxleft -height[left]
                left += 1
            else:
                ans += maxright - height[right]
                right -= 1
        return ans








        
