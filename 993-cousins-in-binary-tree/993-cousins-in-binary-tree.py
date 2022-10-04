class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        parentD = {}
        levelOfXAndY = set({})
        nodes = []
        
        def dfs(node, parent, level):
            if node:
                if node.val == x or node.val == y:
                    nodes.append(node)
                    levelOfXAndY.add(level)
                parentD[node] = parent
                dfs(node.left, node, level+1)
                dfs(node.right, node, level+1)
        
        dfs(root, None, 0)
        
        if len(levelOfXAndY) == 1 and parentD[nodes[0]] != parentD[nodes[1]]:
            return True
        else:
            return False