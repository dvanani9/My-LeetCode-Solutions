class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        cur_sum = 0
        def dfs(node):
            nonlocal cur_sum
            if not node:
                return                      
            dfs(node.right)         
            node.val += cur_sum      # Keep traverse until arrive at the right node, update value     
            cur_sum = node.val       # Remember the sum so far            
            dfs(node.left)           # Continue on the left node
            
        dfs(root)       
        return root