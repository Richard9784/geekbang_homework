from typing import List
import collections
#BFS
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0:
            return []
        dic = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        deque = collections.deque()
        deque.append("")
        for i in range(n):
            level = len(deque)
            for j in range(level):
                curr_alpha = dic[digits[i]]
                curr_deque_alpha = deque.popleft()
                for alpha in curr_alpha:
                    deque.append(curr_deque_alpha+alpha)
        return list(deque)

#python技巧
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        conversion={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        if len(digits)==0:
            return [] 
        res = ['']
        for k in digits:
            res =[i+j for i in res for j in conversion[k]]
        return res

#回溯
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        ans = []
        digi_match_alpha = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        def dfs(i, digits, ans, tmp):
            if i == len(digits):
                ans.append(tmp)
                return
            for ch in digi_match_alpha[digits[i]]:
                dfs(i+1, digits, ans, tmp+ch)
        dfs(0, digits, ans, "")
        return ans        

# if __name__ == "__main__":
#     solution = Solution()
#     digits = "23"
#     solution.letterCombinations(digits)