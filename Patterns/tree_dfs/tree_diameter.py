class TreeNode:
    def __init__(self, val, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right


class Solution:
    def dfs(self,node):
        if not node:
            return 0

        path_length_left = self.dfs(node.left)
        path_length_right = self.dfs(node.right)

        current_len = path_length_left + path_length_right + 1

        self.treeDiameter = max(current_len, self.treeDiameter)

        return max(path_length_left, path_length_right) + 1


    def findDiameter(self, root):
      self.treeDiameter = 0

      self.dfs(root)

      return self.treeDiameter


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(6)
    root.right.left = TreeNode(4)
    print(sol.findDiameter(root))