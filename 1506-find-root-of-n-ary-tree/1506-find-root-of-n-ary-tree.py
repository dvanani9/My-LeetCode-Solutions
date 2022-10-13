class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        ans = 0
        for x in tree:
            ans = ans ^ x.val
            for ch in x.children:
                ans = ans ^ ch.val
        
        for node in tree:
            if node.val == ans:
                return node