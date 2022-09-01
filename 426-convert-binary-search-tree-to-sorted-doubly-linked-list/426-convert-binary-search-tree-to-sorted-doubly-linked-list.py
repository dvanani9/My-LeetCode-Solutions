class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if root is None:
            return root
        
        res, stack = [], []
        cur = root
        
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur)
            cur = cur.right
        
        for i in range(1, len(res)):
            res[i].left = res[i - 1]
        
        for i in range(len(res) - 1):
            res[i].right = res[i + 1]
        
        res[0].left = res[-1]
        res[-1].right = res[0]
        
        return res[0]
    
    