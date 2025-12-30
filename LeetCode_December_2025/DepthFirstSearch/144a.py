from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr = root
        stack, res = [], []
        while curr or stack:
            if curr:
                res.append(curr.val)
                stack.append(curr)
                curr = curr.left  
            else:
                curr = stack.pop()
                curr = curr.right 

        return res              



tn2 = TreeNode(2)
tn3 = TreeNode(3, left=tn2)
tn5 = TreeNode(5)
tn7 = TreeNode(7)
tn6 = TreeNode(6, left=tn5, right=tn7)
root = TreeNode(4, left=tn3, right=tn6)

node = Solution().preorderTraversal(root)
if node:
    print(node)
else:
    print(node)