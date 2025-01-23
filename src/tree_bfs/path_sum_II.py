# Leetcode 113 Path Sum II

from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []

        result = []
        q = deque()
        path = [root.val]
        q.append((root,root.val,path))

        while q:
            current_node, current_sum , current_path = q.popleft()

            if not current_node.left and not current_node.right and current_sum == targetSum:
                result.append(current_path)

            if current_node.left:
                q.append((current_node.left, current_sum + current_node.left.val,current_path + [current_node.left.val]))

            if current_node.right:
                q.append((current_node.right, current_sum + current_node.right.val,current_path + [current_node.right.val]))

        return result

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
    root.right.right.left = TreeNode(5)
    print("Level order traversal: " + str(sol.pathSum(root,22)))







