# Status: Not Bad

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# For now I know only BFS
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        queue = [cloned]
        while queue:
            node = queue.pop(0)
            if node.val == target.val:
                return node
            if node.right != None:
                queue.append(node.right)
            if node.left != None:
                queue.append(node.left)

        return None
# tree = [7,4,3,null,null,6,19], target = 3
four_ = TreeNode(4)
six_ = TreeNode(6)
nineteen_ = TreeNode(19)
target = TreeNode(3)
target.left, target.right = six_, nineteen_
original = TreeNode(7)
original.left, original.right = four_, target


four = TreeNode(4)
six = TreeNode(6)
nineteen = TreeNode(19)
three = TreeNode(3)
three.left, three.right = six, nineteen
cloned = TreeNode(7)
cloned.left, cloned.right = four, three

solve = Solution()
answ = solve.getTargetCopy(original,cloned,target)
print(answ.val)
