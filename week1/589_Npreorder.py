"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
#递归
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res= []
        def dfs(root):
            if not root:return
            res.append(root.val)
            children = root.children
            for child in children:
                dfs(child)
        dfs(root)
        return res
#迭代
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            stack.extend(node.children[::-1])
        return res