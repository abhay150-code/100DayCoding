# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def func(node):
            if not node:
                return
            func(node.left)
            result.append(node.val)
            func(node.right)
        
        func(root)
        return result