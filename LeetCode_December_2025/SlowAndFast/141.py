from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False 
    def hasCycle_2(self, head: Optional[ListNode]) -> bool:
        hset = set()
        while head:
            if head in hset:
                return True
            hset.add(head)
            head = head.next
        return False
    


hset = set()
n1 = ListNode(1)
n2 = ListNode(1)
print(hash(n1))
print(hash(n2))
hset.add(n1)
hset.add(n2)
print(hset)
print(type(n1))
if n1 in hset:
    print('hi')