from typing import *
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        node = self.reverseList(head.next)     
        head.next.next = head
        head.next = None

        return node



ln5 = ListNode(5, next=None)  
ln4 = ListNode(4, next=ln5)
ln3 = ListNode(3, next=ln4)
ln2 = ListNode(2, next=ln3)
ln1 = ListNode(1, next=ln2)

rvr = Solution().reverseList
ln = rvr(ln1)
i = 5
while i > 0:
    print(ln.val)
    ln = ln.next
    i -= 1