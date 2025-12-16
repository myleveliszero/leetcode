from typing import *
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        lst = [head]
        while head.next != None:
            lst.append(head.next)
            head = head.next
        
        lst[0].next = None
        for i in range(len(lst)-1,0,-1):
            lst[i].next = lst[i-1]

        return lst[-1]

ln5 = ListNode(5, next=None)  
ln4 = ListNode(4, next=ln5)
ln3 = ListNode(3, next=ln4)
ln2 = ListNode(2, next=ln3)
ln1 = ListNode(1, next=ln2)

rvr = Solution().reverseList
ln = rvr(None)
print(ln.val)
print(ln.next.val)
print(ln.next.next.val) 