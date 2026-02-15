class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findPaths(self, root, required_sum):
        allPaths = []
        current_path = []

        def dfs(node, remaining_sum, path):
            if node is None:
                return []

            path.append(node.val)

            if not node.left and not node.right and node.val == remaining_sum:
                # Create a new list for the valid path (important!)
                allPaths.append(path[:])

            dfs(node.left, remaining_sum - node.val, path)
            dfs(node.right, remaining_sum - node.val, path)

            path.pop()

        dfs(root,required_sum,current_path)
        return allPaths


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(9)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(7)
    print("Path sum: " + str(sol.findPaths(root,12)))