from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inOrderTraverse(root, lst):
            if root is None:
                return root

            if root.left is not None:
                inOrderTraverse(root.left, lst)
            
            lst.append(root.val)
            if root.right is not None:
                inOrderTraverse(root.right, lst)

            
            return root

        lst = []
        inOrderTraverse(root, lst)
        return lst



tn2 = TreeNode(2)
tn3 = TreeNode(3, left=tn2)
tn5 = TreeNode(5)
tn7 = TreeNode(7)
tn6 = TreeNode(6, left=tn5, right=tn7)
root = TreeNode(4, left=tn3, right=tn6)

node = Solution().inorderTraversal(root)
if node:
    print(node)
else:
    print(node)