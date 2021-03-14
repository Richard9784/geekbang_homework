# # Definition for a Node.
# class Node:
#     def __init__(self, val=None, children=None):
#         self.val = val
#         self.children = children
#迭代
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            stack.extend(node.children)
        return res[::-1]
#递归
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        def dfs(root):
            if not root:return
            children = root.children
            for child in children:
                dfs(child)
            res.append(root.val)
        dfs(root)
        return res

