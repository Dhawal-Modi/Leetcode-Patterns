# Leetcode 112 Path sum
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
from collections import deque

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        q = deque()
        q.append((root,root.val))

        while q:
            level_size = len(q)

            for _ in range(level_size):
                current_node, current_sum = q.popleft()

                if not current_node.left and not current_node.right and current_sum == targetSum:
                    return True

                if current_node.left:
                    q.append((current_node.left,current_sum + current_node.left.val))

                if current_node.right:
                    q.append((current_node.right,current_sum + current_node.right.val))

        return False

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)
    print("Level order traversal: " + str(sol.hasPathSum(root,22)))