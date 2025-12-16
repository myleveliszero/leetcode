from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def binTree(preorder, inorder, left, right, curIdx):
            nxt_idx = None
            for idx in range(left, right):
                if inorder[idx] == preorder[curIdx]:
                    nxt_idx = idx
                    break
            if nxt_idx is None:
                return (None, curIdx)

            root = TreeNode(preorder[curIdx])
            curIdx += 1
            left_node, curIdx = binTree(preorder, inorder, left, nxt_idx, curIdx)
            root.left = left_node
            right_node, curIdx = binTree(preorder, inorder, nxt_idx+1, right, curIdx)
            root.right = right_node
            
            return (root, curIdx)

        root, _ = binTree(preorder, inorder, left=0, right=len(inorder), curIdx=0)
        return root 


# tn2 = TreeNode(2)
# tn3 = TreeNode(3, left=tn2)
# tn5 = TreeNode(5)
# tn7 = TreeNode(7)
# tn6 = TreeNode(6, left=tn5, right=tn7)
# root = TreeNode(4, left=tn3, right=tn6)
# # root = TreeNode(596)

preorder = [1,2,3,4,5,6,7,8,9]
inorder = [3,2,5,4,6,1,8,7,9]
# inorder = [1,2,4,3,5]
# preorder = [1,2,3,4,5]

node = Solution().buildTree(preorder, inorder)
if node:
    print(node.val)
else:
    print(node)