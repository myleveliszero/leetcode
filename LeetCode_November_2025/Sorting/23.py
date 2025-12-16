from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lst_vals = []
        while lists:
            node = lists.pop()
            while node:
                lst_vals.append(node.val)
                node = node.next
        if lst_vals:
            lst_vals.sort()
            dummy = head = ListNode()
            for i in range(len(lst_vals)):
                head.next = ListNode(val=lst_vals[i])
                head = head.next 
            return dummy.next

 
