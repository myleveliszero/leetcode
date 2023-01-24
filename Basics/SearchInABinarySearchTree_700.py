# Status: Not Bad

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# For now I only know BFS
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        que = [root]
        while que:
            node = que.pop(0)
            if node.val == val:
                return node
            if node.left != None:
                que.append(node.left)
            if node.right != None:
                que.append(node.right)
        return None

one = TreeNode(1)
three = TreeNode(3)
two = TreeNode(2, left=one, right=three)
seven = TreeNode(7)
root = TreeNode(4, left=two, right=seven)

solve = Solution()
res = solve.searchBST(root, 2)
if res != None:
    que = [res]
    while que:
        node = que.pop(0)
        print(node.val, end=' ')
        if node.left != None:
            que.append(node.left)
        if node.right != None:
            que.append(node.right)
print()


    