from typing import *
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None
        elif list1 == None:
            return list2
        elif list2 == None: 
            return list1

        if list1.val > list2.val:
            head = list2
            list2 = list2.next
        else:
            head = list1
            list1 = list1.next

        ans = head

        while list1 and list2:
            if list1.val > list2.val:
                head.next = list2
                head = head.next
                list2 = list2.next
            else:
                head.next = list1
                head = head.next
                list1 = list1.next
        if list1:
            head.next = list1
        elif list2:
            head.next = list2

        return ans


ln4 = ListNode(4, next=None)
# ln3 = ListNode(3, next=ln4)
ln2 = ListNode(2, next=ln4)
ln1 = ListNode(1, next=ln2)

ln24 = ListNode(4, next=None)
ln23 = ListNode(3, next=ln24)
# ln22 = ListNode(2, next=ln3)
ln21 = ListNode(1, next=ln23)


rvr = Solution().mergeTwoLists
ln = rvr(ln1, ln21)
print(ln.val)
print(ln.next.val)
print(ln.next.next.val) 