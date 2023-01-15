# Status: Good

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        answ = 0
        while head:
            answ = answ << 1 | head.val # answ*2+head.val
            head = head.next
        return answ

third = ListNode(1)
second = ListNode(0, next=third)
head = ListNode(1, next=second)

solve = Solution()
print(solve.getDecimalValue(head))