# Leetcode 404 Sum of left leaves
from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]):
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 0

        def isLeaf(node: TreeNode) -> bool:
            return node and not node.left and not node.right

        q = deque()
        q.append(root)

        result = 0

        while q:
            current_level = []
            level_size = len(q)

            for _ in range(level_size):
                current_node = q.popleft()
                current_val = current_node.val

                current_level.append(current_val)

                if current_node.left and (isLeaf(current_node.left)):
                    result += current_node.left.val

                if current_node.left:
                    q.append(current_node.left)

                if current_node.right:
                    q.append(current_node.right)

        return result


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print("Sum of left leaves: " + str(sol.sumOfLeftLeaves(root)))

    root = TreeNode(1)
    root.right = TreeNode(2)
    print("Sum of left leaves: " + str(sol.sumOfLeftLeaves(root)))

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    print("Sum of left leaves: " + str(sol.sumOfLeftLeaves(root)))