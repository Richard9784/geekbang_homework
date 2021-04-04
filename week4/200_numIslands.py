#dfs
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i,j):
            if not 0 <= i < len(grid) or not 0 <= j < len(gird[0]) or grid[i][j] == "0":
                return
            grid[i][j] = "0"
            for dx, dy in [[-1,0],[1,0],[0,1],[0,-1]]:
                tmp_i, tmp_j = i + dx, j + dy
                dfs(tmp_i,tmp_j)
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                dfs(i,j)
                count += 1
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
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ocean = 0
        uf = UnionFind(m*n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    ocean += 1
                else:
                    if i+1 < m and grid[i+1][j] == "1":
                        uf.union((i+1)*n+j,i*n+j)
                    if j+1 < n and grid[i][j+1] == "1":
                        uf.union(i*n+j+1,i*n+j)
        return uf.size - ocean