# Status: Not Bad

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        queue = [root]
        answ = 0
        while queue:
            node = queue.pop(0)
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)

            if node.val % 2 == 0:
                if node.left != None:
                    if node.left.left != None:
                        answ += node.left.left.val
                    if node.left.right != None:
                        answ += node.left.right.val
                if node.right != None:
                    if node.right.right != None:
                        answ += node.right.right.val
                    if node.right.left != None:
                        answ += node.right.left.val

        return answ 

five = TreeNode(5)
six = TreeNode(6)
seven = TreeNode(7, left=six, right= five)
four = TreeNode(4, right=seven)
three = TreeNode(3, right=four)
root = TreeNode(2, left=three)

solve = Solution()
print(solve.sumEvenGrandparent(root))