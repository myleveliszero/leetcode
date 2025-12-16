from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def postOrderTraverse(root, lst):
            if root is None:
                return root
            postOrderTraverse(root.left, lst)
            postOrderTraverse(root.right, lst)
            lst.append(root.val)

            return root

        lst = []
        postOrderTraverse(root, lst)
        return lst



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