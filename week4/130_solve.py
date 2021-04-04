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
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:return
        m = len(board)
        n = len(board[0])
        uf = UnionFind(m*n+1)
        dummy = m*n

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    if i == 0 or i == m-1 or j == 0 or j == n-1:
                        uf.union(i*n+j,dummy)
                    else:
                        for x,y in [[1,0],[-1,0],[0,1],[0,-1]]:
                            if board[i+x][j+y] == "O":
                                uf.union(i*n+j,(i+x)*n+j+y)
        
        for i in range(m):
            for j in range(n):
                if uf.find(dummy) == uf.find(i * n + j):
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"




