class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        
        prev = ListNode(0, None)
        
        node = head
        
        stack = collections.deque([])
        
        while node:
            
            stack.appendleft(node)
            
            if node.next is None:
                if node.val == 9:
                    
                    carry = 1
                    
                    for oldnode in stack:
                        if oldnode.val == 9:
                            oldnode.val = 0
                        else:
                            carry = 0
                            oldnode.val = oldnode.val + 1
                            break
                    
                    if carry > 0:
                        new_head = ListNode(1, head)
                        return new_head
                    
                else:
                    node.val = node.val + 1
            
            prev = node
            node = node.next
            
        return head