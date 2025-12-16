from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorderTraversal(root, lst):
            if root is None:
                return root
            inorderTraversal(root.left, lst)
            lst.append(root.val)
            inorderTraversal(root.right, lst)

        lst = [-1]
        inorderTraversal(root, lst)
        return lst[k]

tn2 = TreeNode(2)
tn3 = TreeNode(3, left=tn2)
tn5 = TreeNode(5)
tn7 = TreeNode(7)
tn6 = TreeNode(6, left=tn5, right=tn7)
# root = TreeNode(4, left=tn3, right=tn6)
root = TreeNode(596)

node = Solution().kthSmallest(root, 1)
if node:
    print(node)
else:
    print(node)
