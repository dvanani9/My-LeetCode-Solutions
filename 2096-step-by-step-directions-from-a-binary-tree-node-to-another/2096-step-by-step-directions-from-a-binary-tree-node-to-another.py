class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def dfs(node, path, val) :
            if node.val == val :
                return True
            
            if node.left and dfs(node.left, path, val) :
                path.append('L')
                
            elif node.right and dfs(node.right, path, val) :
                path.append('R')
                
            return len(path) > 0 # failed to find a path
        
        start, dest = [], []
        
        dfs(root, start, startValue) # create a start node path
        dfs(root, dest, destValue) # create a dest node path
        
        while start and dest and start[-1] == dest[-1] :
            start.pop()
            dest.pop()
        
        return 'U'*len(start) + ''.join(reversed(dest))