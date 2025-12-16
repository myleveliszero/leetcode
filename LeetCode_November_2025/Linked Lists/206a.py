from typing import *
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = None
        while head:
            next_node = head.next
            head.next = node
            node = head
            head = next_node
        
        return node 




ln5 = ListNode(5, next=None)  
ln4 = ListNode(4, next=ln5)
ln3 = ListNode(3, next=ln4)
ln2 = ListNode(2, next=ln3)
ln1 = ListNode(1, next=ln2)

rvr = Solution().reverseList
ln = rvr(ln1)
print(ln.val)
print(ln.next.val)
print(ln.next.next.val) 