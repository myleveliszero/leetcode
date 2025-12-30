from typing import List

class TreeNode:
    def __init__(self, total, l_idx, r_idx):
        self.total = total
        self.l_idx = l_idx
        self.r_idx = r_idx
        self.left = None
        self.right = None

class NumArray:

    def __init__(self, nums: List[int]):
        def dc(nums, left, right):
            if right-left <= 0:
                return TreeNode(nums[left], left, right)
            mid = (right+left)//2
            node = TreeNode(0, left, right)
            node.left = dc(nums, left, mid)
            node.right = dc(nums, mid+1, right)
            node.total = node.left.total + node.right.total
            return node

        self.root = dc(nums, 0, len(nums)-1)


    def update(self, index: int, val: int) -> None:
        def dfs(root, idx, val):
            mid = (root.r_idx+root.l_idx)//2
            if root.l_idx == idx and root.r_idx == idx:
                root.total = val
                return 
            if root.l_idx <= idx <= mid:
                dfs(root.left, idx, val)
            else:
                dfs(root.right, idx, val)
            
            root.total = root.left.total + root.right.total
            return root   
        
        dfs(self.root, index, val)

    def sumRange(self, left: int, right: int) -> int:
        def dfs(root, left, right):
            if root.l_idx == left and root.r_idx == right:
                return root.total
            
            mid = (root.l_idx+root.r_idx)//2
            
            if right <= mid:
                return dfs(root.left, left, right)
            elif left >= mid+1:
                return dfs(root.right, left, right)
            else:
                val1= dfs(root.left, left, mid)
                val2= dfs(root.right, mid+1, right)
                return val1+val2

             

        return dfs(self.root, left, right)


def test(op, input):
    obj = eval(f"{op[0]}({input[0][0]})")
    for i in range(1, len(input)):
        # if not input[i]:
        #     print(eval(f"obj.{op[i]}()"))
        print(eval(f"obj.{op[i]}({input[i][0]}, {input[i][1]})"))

op = ["NumArray", "update", "update", "sumRange", "sumRange", "sumRange"]
inp = [[[5,3,7,1,4,2]], [0, 1], [5, 5], [2,4], [0, 0], [5,5]]

test(op, inp)