class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    tree_val = []
    
    def helper(tree):
      if tree:
        helper(tree.left)
        tree_val.append(tree.val)
        helper(tree.right)
    
    if root:
      helper(root)
    return tree_val