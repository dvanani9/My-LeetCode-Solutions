class Solution:
	def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
		tree = []
		def inorder(root):
			if not root: return None
			inorder(root.left)
			tree.append(root)
			inorder(root.right)
		inorder(root)
		n = len(tree)
		for i in range(n):
			if tree[i] == p: 
				if i < n-1: return tree[i+1]
				else: return None