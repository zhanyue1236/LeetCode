from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left: Optional['TreeNode']=None, right: Optional['TreeNode']=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # 返回一个元组 (rob, not_rob)
        # rob 表示选择当前节点时能够获得的最大金额
        # not_rob 表示不选择当前节点时能够获得的最大金额
        def robNode(root: Optional[TreeNode]) -> (int, int):
            #(rob, norob)
            if not root:
                return (0, 0)
            left = robNode(root.left)
            right = robNode(root.right)
            '''
            yesRob = root.val + left[1] + right[1]

            noRob = max(left[0], right[0])
            '''
            yesRob = root.val + left[1] + right[1]

            noRob = max(left) + max(right)
            
            return (yesRob, noRob)
        (left, right) = robNode(root)
        return max(left, right)

