from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoNodes(first, second):
            dummy = cur = ListNode()
            while first and second:
                if first.val < second.val:
                    cur.next, first = first, first.next
                else:
                    cur.next, second = second, second.next
                cur = cur.next
            if first or second:
                cur.next = first if first else second
            return dummy.next 
            
        
        if len(lists) > 0:
            while len(lists) > 1:
                temp = []
                for i in range(0, len(lists), 2):
                    l1 = lists[i]
                    l2 = lists[i+1] if i+1 < len(lists) else None
                    temp.append(mergeTwoNodes(l1, l2))
                lists = temp             
            
            return lists[0]
        
lists = [[1,4,5],[1,3,4],[2,6]]
ln5 = ListNode(5, None)
ln4 = ListNode(4, ln5)
ln1 = ListNode(1, ln4)

ln42 = ListNode(4, None)
ln32 = ListNode(3, ln42)
ln12 = ListNode(1, ln32)

ln63 = ListNode(6, None)
ln23 = ListNode(2, ln63)

lists = [ln1,ln12,ln23]
node = Solution().mergeKLists(lists)
while node: print(node.val); node = node.next
