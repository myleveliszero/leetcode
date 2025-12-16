from typing import Optional 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right 

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def inorderTraversal(root, lst):
            if root is None:
                return False 
            lst.append(root.val)
            if sum(lst) == targetSum:
                if root.left is None and root.right is None:
                    return True
                                
            l = inorderTraversal(root.left, lst)
            if l: return True
            r = inorderTraversal(root.right, lst)
            if r: return True
            
            lst.pop()
            return False
        
        return inorderTraversal(root, [])



tn2 = TreeNode(2)
tn13 = TreeNode(13)
tn7 = TreeNode(7)
tn1 = TreeNode(3)
tn4 = TreeNode(4, right=tn1)
tn11 = TreeNode(11, tn7, tn2)
tn_4 = TreeNode(4, left=tn11)   
tn8 = TreeNode(8, tn13, tn4)
root = TreeNode(5, tn_4, tn8)

# node = Solution().hasPathSum(root, targetSum=25)
node = Solution().hasPathSum(root, targetSum=20)

print(node)