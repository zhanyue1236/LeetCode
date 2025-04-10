from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Helper function to build a binary tree from a list
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    root = TreeNode(values[0])
    Q = deque([root])
    i = 1
    while Q and i < len(values):
        current = Q.popleft()
        if values[i] is not None:
            current.left = TreeNode(values[i])
            Q.append(current.left)
        i += 1
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            Q.append(current.right)
        i += 1
    return root

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        Q = deque([root])
        res = []
        while Q:
            level = []
            for i in range(len(Q)):
                current = Q.popleft()
                level.append(current.val)  # Append node value
                if current.left:
                    Q.append(current.left)
                if current.right:
                    Q.append(current.right)
            res.append(level)
        return res

# Input tree
tree_values = [3, 9, 20, None, None, 15, 7]
root = build_tree(tree_values)

# Create Solution object and call levelOrder
solution = Solution()
output = solution.levelOrder(root)
print(output)