class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            node = trie
            for c in word:
                node = node.setdefault(c,{})
            node["#"] = True

        def dfs(i,j,cur_word,cur_dict):
            current_char = board[i][j]
            if current_char not in cur_dict:
                return
            cur_word += current_char
            cur_dict = cur_dict[current_char]
            if "#" in cur_dict:
                res.add(cur_word)
            board[i][j] = "0"
            for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                tmp_i, tmp_j = i + dx, j + dy
                if 0 <= tmp_i < m and 0 <= tmp_j < n and board[tmp_i][tmp_j] !="0":
                    dfs(tmp_i,tmp_j,cur_word,cur_dict)
            board[i][j] = current_char

        res, m, n = set(), len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                dfs(i,j,"",trie)
        return list(res)