# from typing import Optional

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         def inorderTraversal(root, k, iter=1):
#             if root is None:
#                 return root
#             inorderTraversal(root.left, k, iter)

#             inorderTraversal(root.right, k, iter)

#         return inorderTraversal(root, k)



# tn2 = TreeNode(2)
# tn3 = TreeNode(3, left=tn2)
# tn5 = TreeNode(5)
# tn7 = TreeNode(7)
# tn6 = TreeNode(6, left=tn5, right=tn7)
# root = TreeNode(4, left=tn3, right=tn6)
# # root = TreeNode(596)

# node = Solution().kthSmallest(root, 5)
# if node:
#     print(node)
# else:
#     print(node)
