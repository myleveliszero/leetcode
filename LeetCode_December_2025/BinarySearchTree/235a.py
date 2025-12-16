# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root


tn1 = TreeNode(1)
tn3 = TreeNode(3)
tn7 = TreeNode(7)
tn2 = TreeNode(2, left=tn1, right=tn3)
t4 = TreeNode(4, tn2, tn7)

node = Solution().lowestCommonAncestor(t4, tn1, tn3)
if node:
    print(node.val)
else:
    print(node)