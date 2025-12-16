# Status: Not Bad

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# For now I know only BFS
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        queue = [root]
        while queue:
            answ = 0
            temp = []
            for node in queue:
                answ += node.val
                if node.left != None:
                    temp.append(node.left)
                if node.right != None:
                    temp.append(node.right)
            queue = temp    
        return answ

eight = TreeNode(8)
seven = TreeNode(7)
six = TreeNode(6, right=eight)
five = TreeNode(5)
four = TreeNode(4, left=seven)
three = TreeNode(3, right=six)
two = TreeNode(2, left=four,right=five)
root = TreeNode(1, left=two, right=three)

solve = Solution()
print(solve.deepestLeavesSum(root))
