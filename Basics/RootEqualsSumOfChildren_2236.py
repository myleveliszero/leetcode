# Status: Good

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def checkTree(self, root: TreeNode) -> bool:
        return True if root.left.val+root.right.val == root.val else False
        
five = TreeNode(5)
six = TreeNode(6)
root = TreeNode(12,left=five,right=six)
solve = Solution()
print(solve.checkTree(root))

five = TreeNode(5)
six = TreeNode(6)
root = TreeNode(11, left=six, right=five)
print(solve.checkTree(root))