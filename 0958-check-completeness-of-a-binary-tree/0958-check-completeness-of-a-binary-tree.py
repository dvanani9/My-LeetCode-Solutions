from collections import deque

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        
        
        traversal_queue = deque( [ root ] )
        prev_node = root
        
        
        # Launch Level-order traversal
        
        while traversal_queue:
            
            cur_node = traversal_queue.popleft()
            
            if cur_node:
                
                if not prev_node:
                    # Empty node in the middle means this is not a complete binary tree ( not left-compact)
                    return False
                
                traversal_queue.append( cur_node.left )
                traversal_queue.append( cur_node.right )
            
            # update previous node
            prev_node = cur_node
            
        return True