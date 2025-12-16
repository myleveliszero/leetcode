from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def findMinNode(self, node):
        while node.left is not None:
            node = node.left
        return node

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root
        
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            # case 1: when node has 0 or 1 child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            # case 2: when node has 2 child
            else:
                # find min node in right subtree
                node = self.findMinNode(root.right)
                root.val = node.val
                root.right = self.deleteNode(root.right, node.val)

        return root 


tn2 = TreeNode(2)
tn3 = TreeNode(3, left=tn2)
tn5 = TreeNode(5)
tn7 = TreeNode(7)
tn6 = TreeNode(6, left=tn5, right=tn7)
root = TreeNode(4, left=tn3, right=tn6)
# tn2 = TreeNode(2, left=tn1, right=tn3)

node = Solution().deleteNode(root, 8)
if node:
    print(node)
else:
    print(node)