class Node(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return str(self.val) 
    
class Solution(object):
    def reverseList(self, head):
        prev = None 
        curr = head
        while curr:
            nxt = curr.next 
            curr.next = prev
            prev = curr
            curr = nxt 
        return prev 
            
