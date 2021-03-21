#DFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:return 0
        m = len(grid)
        n = len(grid[0])
        count = 0
        def helper(i,j):
            if i < 0 or j < 0 or i >=m or j >= n or grid[i][j] != "1":
                return 
            grid[i][j] = "0"
            helper(i,j-1)
            helper(i,j+1)
            helper(i+1,j)
            helper(i-1,j)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    helper(i,j)
                    count += 1
        return count

import collections
#BFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:return 0
        m = len(grid)
        n = len(grid[0])
        count = 0
        def helper(i,j):
            queue = collections.deque()
            queue.append((i,j))
            grid[i][j] = "0"
            while queue:
                i, j = queue.popleft()
                for x, y in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    tmp_i = i + x
                    tmp_j = j + y
                    if 0 <= tmp_i < row and 0 <= tmp_j < col and grid[tmp_i][tmp_j] == "1":
                        grid[tmp_i][tmp_j] = "0"
                        queue.appendleft((tmp_i, tmp_j))


        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    helper(i,j)
                    count += 1
        return count


