#DFS
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(x):
            visited[x] = 1
            for j in range(n):
                if isConnected[x][j] == 1 and not visited[j]:
                    dfs[j]
        
        n = len(isConnected)
        visited = [0] * n
        count = 0
        for i in range(n):
            if not visited[i]:
                count += 1
                dfs(i)
        
        return count

#BFS
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def bfs(root):
            queue = collections.deque()
            queue.append(root)

            while queue:
                u = queue.popleft()
                for v in range(n):
                    if isConnected[u][v] == 1 and not visited[v]:
                        visited[v] = 1
                        queue.append(v)

        n = len(isConnected)
        visited = [0] * n
        count = 0
        for i in range(n):
            if not visited[i]:
                count += 1
                visited[i] = 1
                bfs(i)
        
        return count

#并查集
class UnionFind:
    def __init__(self,n):
        self.size = n
        self.p = [i for i in range(n)]

    def find(self,i):
        root = i
        while self.p[root] != root:
            root = self.p[root]
        while self.p[i] != i:
            x = i
            self.p[x] = root
            i = self.p[i]
        return root
    
    def union(self,a,b):
        ar, br = self.find(a), self.find(b)
        if ar != br:
            self.p[ar] = br
            self.size -= 1

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j] == 1:
                    uf.union(i,j)
        return uf.size

            
                