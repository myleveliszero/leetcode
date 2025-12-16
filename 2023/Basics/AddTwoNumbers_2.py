# Status: Not Bad

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        i, j = "", ""
        while l1:
            i = str(l1.val) + i 
            l1 = l1.next
        while l2:
            j = str(l2.val) + j
            l2 = l2.next 
        
        n = str(int(i)+int(j))[::-1]
        head = cur = ListNode(n[0])
        for k in range(1, len(n)):
            cur.next = ListNode(n[k])
            cur = cur.next
        return head


three = ListNode(3, None)
four = ListNode(4, three)
two = ListNode(2, four)

first = ListNode(4, None)
second = ListNode(6, first)
third = ListNode(5, second)

solve = Solution()

ans = solve.addTwoNumbers(two, third)
while ans:
    print(ans.val)
    ans = ans.next