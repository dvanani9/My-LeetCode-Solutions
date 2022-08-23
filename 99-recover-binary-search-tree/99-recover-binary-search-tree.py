# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        temp = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            temp.append(node)
            dfs(node.right)

        dfs(root)

        srt = sorted(n.val for n in temp)
        
        for i in range(len(srt)):
            temp[i].val = srt[i]

        