# Status: Good


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while True:
            if fast.next == None:
                return slow
            elif fast.next.next == None:
                return slow.next
            slow = slow.next
            fast = fast.next.next

five = ListNode(val=5, next=None)
four = ListNode(val=4, next=five)
three = ListNode(val=3, next= four)
two = ListNode(val=2, next=three)
one = ListNode(val=1, next=two)

solve  = Solution()
ans = solve.middleNode(one)

print(ans.val)