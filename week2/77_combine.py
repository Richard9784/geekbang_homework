class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(i,tmp):
            if len(tmp) == k:
                res.append(tmp)
                return
            for j in range(i,n+1):
                backtrack(j+1,tmp+[j])
        backtrack(1,[])
        return res
