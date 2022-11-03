class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def getLeaves(root):
            q=deque([root])
            while q:
                leaves=[]    
                for i in range(len(q)):
                    node=q.popleft()
                    leaves.append(node)
                    
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            return leaves
        
        leaves=getLeaves(root)
        leaves=set(leaves)
        
        def getLCA(root):
            if not root:return
            if root in leaves:
                return root
            left=getLCA(root.left)
            right=getLCA(root.right)
            return root if left and right else left or right
        
        return getLCA(root)