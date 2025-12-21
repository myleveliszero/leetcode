from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        node = None # reverse node
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            next_node = slow.next 
            slow.next = node 
            node = slow
            slow = next_node
    
        max_val = 0
        while slow is not None:
            # max_val = max(max_val, slow.val+node.val)
            if max_val < slow.val+node.val:
                max_val = slow.val+node.val
            slow = slow.next
            node = node.next
        
        return max_val


ln6 = ListNode(6, )
ln1 = ListNode(1, ln6)
ln3 = ListNode(3, ln1)
ln2 = ListNode(2, ln3)
ln4 = ListNode(4, ln2)
ln5 = ListNode(5, ln4)

sol = Solution().pairSum
print(sol(ln5))