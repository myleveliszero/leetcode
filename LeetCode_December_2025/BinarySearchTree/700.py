from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:        
        if not root or root.val == val:
            return root
        if root.val > val:
            node = self.searchBST(root.left, val)
        else:
            node = self.searchBST(root.right, val)
  
        return node
    
tn1 = TreeNode(1)
tn3 = TreeNode(3)
tn7 = TreeNode(7)
tn2 = TreeNode(2, left=tn1, right=tn3)
t4 = TreeNode(4, tn2, tn7)

node = Solution().searchBST(t4, 5)
if node:
    print(node.val)
else:
    print(node)
