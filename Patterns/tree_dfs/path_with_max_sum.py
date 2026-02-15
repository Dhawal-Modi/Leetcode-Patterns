class TreeNode:
    def __init__(self, val, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

class Solution:
    def dfs(self,root):


    def max_path_sum(self,root):
        pass



if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(9)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(3)
    print("Max Path sum: " + str(sol.max_path_sum(root)))







