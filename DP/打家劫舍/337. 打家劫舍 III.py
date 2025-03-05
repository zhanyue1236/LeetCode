from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left: Optional['TreeNode']=None, right: Optional['TreeNode']=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # 这里你原先的 tracking 代码只是打印节点值
        node = []
        def tracking(root: Optional[TreeNode]):
            if not root:
                return
            if root.left and root.right:
                tracking(root.left)
                node.append(root.val)
                tracking(root.right)
                return
            elif root.left:
                tracking(root.left)
                node.append(root.val)
                return
            elif root.right:
                tracking(root.right)
                node.append(root.val)
                return
            else:
                node.append(root.val)
        tracking(root)
        print(node)
        return 0  # 这里返回 0 只是示例

# 辅助函数：根据列表构造二叉树（层序构造）
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while i < len(values):
        current = queue.pop(0)
        if current:
            if i < len(values):
                if values[i] is not None:
                    current.left = TreeNode(values[i])
                queue.append(current.left)
                i += 1
            if i < len(values):
                if values[i] is not None:
                    current.right = TreeNode(values[i])
                queue.append(current.right)
                i += 1
    return root

# 构造输入二叉树，输入：[3,2,3,None,3,None,1]
tree_values = [3, 2, 3, None, 3, None, 1]
root = build_tree(tree_values)

S = Solution()
S.rob(root)