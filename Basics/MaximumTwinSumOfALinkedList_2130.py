# Status: Not Bad

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: ListNode) -> int:
        sequence = []
        while head:
            sequence.append(head.val)
            head = head.next
        answ = []
        for i in range(len(sequence)//2):
            answ.append(sequence[i]+sequence[~i])
        return max(answ)

one = ListNode(1)
two = ListNode(2, next=one)
four = ListNode(4, next=two)
five = ListNode(5, next=four)

solve = Solution()
print(solve.pairSum(five))
