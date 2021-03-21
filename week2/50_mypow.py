#分治法
class Solution(object):
    def myPow(self, x, n):
        def helper(x,n):
            if n == 0:return 1
            if n == 1:return x
            y = helper(x,n//2)
            if n % 2:
                return x*y*y
            else:
                return y*y
        if n<0:return 1/self.myPow(x,-n)
        return helper(x,n)