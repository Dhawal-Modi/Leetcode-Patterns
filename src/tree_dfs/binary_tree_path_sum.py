#Leetcode 112 Path Sum(Can also be solved with tree bfs)

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPath(self, root, sum):
        if root is None:
            return False

        if not root.left and not root.right and root.val == sum:
            return True

        left_sum = self.hasPath(root.left, sum - root.val)
        right_sum = self.hasPath(root.right, sum - root.val)

        if left_sum or right_sum:
            return True
        return False

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print("Path sum: " + str(sol.hasPath(root,10)))