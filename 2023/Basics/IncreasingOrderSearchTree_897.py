# Status: Not Bad

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# For now I only know BFS
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        que = [root]
        answ = []
        while que:
            node = que.pop(0)
            answ.append(node.val)
            if node.left != None:
                que.append(node.left)
            if node.right != None:
                que.append(node.right)
        answ.sort()
        root = prev = TreeNode(answ[0])
        for i in range(1, len(answ)):
            node = TreeNode(answ[i])
            prev.right = node
            prev = node
        return root

one = TreeNode(1)
two = TreeNode(2, left=one)
four = TreeNode(4)
three = TreeNode(3, left=two, right=four)
six = TreeNode(6)
root1 = TreeNode(5, left=three, right=six)

solve = Solution()
res = solve.increasingBST(root=root1)
while res:
    print(res.val, end = " ")
    res = res.right
print()
