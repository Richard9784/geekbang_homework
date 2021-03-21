from typing import List
from collections import defaultdict
import collections
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList.append(beginWord)
        m = len(beginWord)
        ### 构建具有邻接关系的桶
        buckets = defaultdict(list)
        for word in wordList:
            for i in range(m):
                match = word[:i] + '_' + word[i+1:]
                buckets[match].append(word)
        ##### BFS遍历
        preWords = defaultdict(list)  # 前溯词列表
        queue = collections.deque()
        queue.append((beginWord,1))  # 待遍历词及深度
        visited = {beginWord:1}  # 已探测词列表
        while queue:
            cur, step = queue.popleft()
            for i in range(m):
                match = cur[:i] + '_' + cur[i+1:]
                for word in buckets[match]:
                    if word not in visited:
                        visited[word] = step+1
                        queue.append((word, step+1))
                    if visited[word] == step+1:  # 当前深度等于该词首次遍历深度，则仍应加入前溯词列表
                        preWords[word].append(cur)
            if endWord in visited and step+1 > visited[endWord]:  # 已搜索到目标词，且完成当前层遍历
                break
        #### 列表推导式输出结果
        if endWord in visited:
            res = [[endWord]]
            while res[0][0] != beginWord:
                
                res = [[word] + r for r in res for word in preWords[r[0]]] 
            return res
        else:
            return []

if __name__ == "__main__":
    solution = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    solution.findLadders(beginWord,endWord,wordList)
