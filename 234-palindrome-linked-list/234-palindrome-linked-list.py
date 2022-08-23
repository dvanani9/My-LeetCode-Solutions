class Solution(object):
    def isPalindrome(self, head):
        test = []
        while head:
            test.append(head.val)
            head = head.next
    
        if test[::-1] == test:
            return True
        return False