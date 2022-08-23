# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import *

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        One interesting thing to find is every level we should have i nodes [1,n]
        
        find nodes in every level and 
        
        '''
        table = defaultdict(list)
        queue = deque([(root,0)])
        
        # bfs
        while queue:
            node, col = queue.popleft()
            
            if node:
                table[col].append(node.val) 
                
                queue.append((node.left, col-1)) # ok ok
                queue.append((node.right,col+1))
                
        return [table[x] for x in sorted(table.keys())]