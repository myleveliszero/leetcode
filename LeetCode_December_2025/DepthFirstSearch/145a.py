from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr = root
        res, stack, visit = [], [], set()
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                if curr.right is None or curr in visit:
                    res.append(curr.val)
                    curr = None
                    continue
                if curr.right is not None:
                    stack.append(curr)
                    visit.add(curr)
                    curr = curr.right

        return res
            



tn2 = TreeNode(2)
tn3 = TreeNode(3, left=tn2)
tn5 = TreeNode(5)
tn7 = TreeNode(7)
tn6 = TreeNode(6, left=tn5, right=tn7)
root = TreeNode(4, left=tn3, right=tn6)

node = Solution().postorderTraversal(root)
if node:
    print(node)
else:
    print(node)