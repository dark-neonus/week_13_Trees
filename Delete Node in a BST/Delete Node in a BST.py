# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root
        # Search for desired node
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        # Found desired node
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            cursor = root.right
            while cursor is not None and cursor.left is not None:
                cursor = cursor.left
            root.val = cursor.val
            root.right = self.deleteNode(root.right, cursor.val)
        return root
