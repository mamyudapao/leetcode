# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        tree_val = []
        
        def helper(tree):
            if tree:
                helper(tree.left)
                helper(tree.right)
                tree_val.append(tree.val)
        helper(root)
        return tree_val