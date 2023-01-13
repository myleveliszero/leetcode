# Status: Not Bad

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# For now I only know BFS
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        queue = [root]
        answ = 0
        while queue:
            node = queue.pop(0)
            # if node.val >= low and node.val <= high:
            if low <= node.val <= high:
                answ += node.val
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
        return answ

three = TreeNode(3)
seven = TreeNode(7)
eighteen = TreeNode(18)
five = TreeNode(val=5,left=three,right=seven)
fifteen = TreeNode(val=15, left=None, right=eighteen)
root = TreeNode(10, five, fifteen)
solve = Solution()
print(solve.rangeSumBST(root, 7, 15))