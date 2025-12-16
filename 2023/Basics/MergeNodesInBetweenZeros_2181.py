# Status: Not Bad

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeNodes(self, head: ListNode) -> ListNode:
        answ = []
        head = head.next
        nsum = 0
        while head:
            val = head.val
            if val == 0:
                answ.append(nsum)
                nsum = 0
            else:
                nsum += val
            head = head.next
        head = node = ListNode()
        for i in answ:
            node.next = ListNode(i)
            node = node.next
        return head.next

zerolast = ListNode(0)
two = ListNode(2, next=zerolast)
four = ListNode(4, next=two)
five = ListNode(5, next=four)
zerosecond = ListNode(0, next=five)
one = ListNode(1, next=zerosecond)
three = ListNode(3, next=one)
head = ListNode(0, next=three)

solve = Solution()
head = solve.mergeNodes(head)
while head:
    print(head.val)
    head = head.next
