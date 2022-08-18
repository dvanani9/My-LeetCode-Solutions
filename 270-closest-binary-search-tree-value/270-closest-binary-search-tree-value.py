class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        
        closest = root.val
        
        while root:
            closest = closest if abs(closest - target) <= abs(root.val - target) else root.val
            root = root.left if target < root.val else root.right
        
        return closest