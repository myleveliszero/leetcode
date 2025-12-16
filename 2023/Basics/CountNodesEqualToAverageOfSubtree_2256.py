# Status: Not bad

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# For know I only know BFS
class Solution:
    def traverseSubtree( self, rootsub):
        queue = [rootsub]
        sumsubT = 0
        counsubT = 0
        while queue:
            node = queue.pop(0)
            sumsubT += node.val
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
            counsubT += 1
        return sumsubT // counsubT

    def averageOfSubtree(self, root: TreeNode) -> int:
        queue = [root]
        answ  = 0
        while queue:
            node = queue.pop(0)
            if node.val == self.traverseSubtree(node):
                answ += 1
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
        return answ
    
zero = TreeNode(0)
one = TreeNode(1) 
six = TreeNode(6)
eight = TreeNode(8, left=zero, right=one)
five = TreeNode(5, right=six)
root = TreeNode(4, left=five, right=eight)

solve = Solution()
print(solve.averageOfSubtree(root))