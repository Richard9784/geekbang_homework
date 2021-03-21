from typing import List
import collections
#DFS
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        direction = ((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(-1,-1),(1,-1))
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board
        self.m, self.n = len(board), len(board[0])
        def check(i, j):
            cnt = 0
            for x, y in direction:
                x, y = x + i, y + j
                if 0 <= x < self.m and 0 <= y < self.n and board[x][y] == "M":
                    cnt += 1
            return cnt
        def dfs(i, j):
            cnt = check(i, j)
            if cnt:
                board[i][j] = str(cnt)
            else:
                board[i][j] = "B"
                for x, y in direction:
                    x, y = x+i, y+j
                    if 0 <= x < self.m and 0 <= y < self.n and board[x][y] == "E":
                        dfs(x,y)


        dfs(click[0], click[1])
        return board

#BFS
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        direction = ((0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1))
        m = len(board)
        n = len(board[0])

        def in_board(x,y):
            return  0 <= x < m and 0 <= y < n
        
        def bfs(x,y):
            visited = [[False]*n for i in range(m)]
            visited[x][y] = True
            queue = collections.deque()
            queue.append((x,y))

            while queue:
                count = 0
                x, y = queue.popleft()
                if board[x][y] == "M":
                    board[x][y] = "X"
                    return
                for i, j in direction:
                    nx, ny = x+i, y+j
                    if in_board(nx, ny) and board[nx][ny] == "M":
                        count += 1
                if count > 0:
                    board[x][y] = str(count)
                else:
                    board[x][y] = "B"
                    for i, j in direction:
                        nx, ny = x+i, y+j
                        if in_board(nx, ny) and visited[nx][ny] != True:
                            queue.append((nx,ny))
                            visited[nx][ny] = True

        bfs(click[0],click[1])
        return board

# if __name__ == "__main__":
#     solution = Solution()
#     board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]
#     click = [3,0]
#     solution.updateBoard(board = board,click= click)