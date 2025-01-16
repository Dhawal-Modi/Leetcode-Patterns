# Leetcode 104 Max depth of binary tree (Easy)

from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0

        max_depth = 0

        q = deque()
        q.append(root)

        while q:
            level_size = len(q)
            max_depth += 1

            for _ in range(level_size):
                current_node = q.popleft()

                if current_node.left:
                    q.append(current_node.left)

                if current_node.right:
                    q.append(current_node.right)

        return max_depth

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print("Level order traversal: " + str(sol.maxDepth(root)))
