from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []
        q, res = [root], []
        while q:
            node = q.pop()
            while node.left:
                q.append(node)
                node = node.left
            
            res.append(node.val)
            while q and node.right is None:
                node = q.pop()
                res.append(node.val)
            if node.right is not None:
                q.append(node.right)       
            
        return res
    
    def inorderTraversal_2(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []
        q, res = [root], []
        while q:
            node = q.pop()
            if node.right is not None:
                q.append(node.right)
            
            q.append(node)
            if node.left is not None:
                q.append(node.left) 
            
            if node.left is None:
                q.pop()
                res.append(node.val)
            node.left = None
            node.right = None
        
        return res


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