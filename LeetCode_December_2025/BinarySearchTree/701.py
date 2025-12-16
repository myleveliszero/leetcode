from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)

        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)

        return root

tn1 = TreeNode(1)
tn3 = TreeNode(3)
tn7 = TreeNode(7)
tn2 = TreeNode(2, left=tn1, right=tn3)
t4 = TreeNode(4, tn2, tn7)

node = Solution().insertIntoBST(t4, 5)
if node:
    print(node.right.left.val)
else:
    print(node)