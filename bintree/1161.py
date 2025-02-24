from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        queue = deque([root])
        res = []
        while queue:
            level = 0
            for i in range(len(queue)):
                current = queue.popleft()
                level += current.val
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            res.append(level)
            #计算最大值下标：res.index(max(res))
        return res.index(max(res)) + 1  # 返回层数，从1开始计数

# Helper function to build a binary tree from a list
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

# Input tree
values = [1, 7, 0, 7, -8, None, None]
root = build_tree(values)

# Call the function
solution = Solution()
output = solution.maxLevelSum(root)
print(output)