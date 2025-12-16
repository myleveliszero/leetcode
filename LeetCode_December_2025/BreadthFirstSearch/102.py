from typing import Optional, List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        lst = []
        que = deque()
        que.append(deque([root]))
        while que and root:
            cur_layer = que.popleft()
            next_layer = deque()
            layer_lst = []

            while cur_layer:
                node = cur_layer.popleft()
                layer_lst.append(node.val)

                if node.left is not None:
                    next_layer.append(node.left)

                if node.right is not None:
                    next_layer.append(node.right)
            if next_layer:
                que.append(next_layer)
            lst.append(layer_lst)
         
        return lst

tn2 = TreeNode(2)
tn3 = TreeNode(3, left=tn2)
tn5 = TreeNode(5)
tn7 = TreeNode(7)
tn6 = TreeNode(6, left=tn5, right=tn7)
root = TreeNode(4, left=tn3, right=tn6)

node = Solution().levelOrder(root)
if node:
    print(node)
else:
    print(node)