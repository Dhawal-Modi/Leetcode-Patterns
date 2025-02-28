class TreeNode:
    def __init__(self, val, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

# class Solution:
#     def dfs(self, node, target_sum, path,all_paths):
#       if node is None:
#         return []
#
#       path.append(node.val)
#
#       current_sum = 0
#
#       for i in range(len(path)-1,-1,-1):
#         current_sum += path[i]
#         if current_sum == target_sum:
#           all_paths.append(path[i:])
#
#       self.dfs(node.left,  target_sum, path,all_paths)
#       self.dfs(node.right, target_sum, path,all_paths)
#
#       path.pop()
#
#     def countPaths(self, root, S):
#       all_paths = []
#       self.dfs(root,S,[],all_paths)
#
#       return len(all_paths)


class Solution:
    def dfs(self, node, target_sum, path,counter):
        if node is None:
            return []

        path.append(node.val)

        current_sum = 0

        for i in range(len(path) - 1, -1, -1):
            current_sum += path[i]
            if current_sum == target_sum:
                counter[0] += 1

        self.dfs(node.left, target_sum, path, counter)
        self.dfs(node.right, target_sum, path, counter)

        path.pop()

    def countPaths(self, root, S):
        counter = [0]
        self.dfs(root, S, [], counter)
        return counter[0]


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(9)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(3)
    print("Path sum: " + str(sol.countPaths(root,12)))