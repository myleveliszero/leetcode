# Status: Not Bad

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        Maintain two pointers and update one with a delay of n steps.
        """
        dummy = head
        length = 1
        while dummy.next:
            dummy = dummy.next
            length += 1
        n = length - n
        ans = rmv = head
        for i in range(n-1):
            rmv = rmv.next
        try:
            if n == 0:
                rmv = rmv.next
            else:
                rmv.next = rmv.next.next
        except: 
            if n == 0:
                return ListNode()
            else:
                rmv.next = None
            
        return ans


five = ListNode(val=5, next=None)
four = ListNode(val=4, next=five)
three = ListNode(val=3, next= four)
two = ListNode(val=2, next=three)
one = ListNode(val=1, next=two)

solve  = Solution()
ans = solve.removeNthFromEnd(head=one, n=5)
print("hi")