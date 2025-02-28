# Leetcode 129 Sum Root to Leaf Numbers

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# My solution
class Solution:
    def findSumOfPathNumbers(self, root):
        if not root:
            return 0

        path = [str(root.val)]
        stack = [(root,path)]
        result = 0
        while stack:
            node , current_path = stack.pop()

            if not node.right and not node.left:
                current_number = int(''.join(current_path))
                result += current_number

            if node.right:
                stack.append((node.right,current_path+ [str(node.right.val)]))
            if node.left:
                stack.append((node.left,current_path + [str(node.left.val)]))

        return result

#My solution DFS recursion
    # def sumNumbers(self, root: Optional[TreeNode]) -> int:
    #     return self.find_root_to_leaf(root,0)
    #
    # def find_root_to_leaf(self, node, path_sum):
    #     if not node:
    #         return 0
    #     path_sum = path_sum * 10 + node.val
    #
    #     if not node.right and not node.left:
    #         return path_sum
    #
    #     return self.find_root_to_leaf(node.left, path_sum) + self.find_root_to_leaf(node.right, path_sum)

#Claude's solution
# def findSumOfPathNumbers(self, root):
#     if not root:
#         return 0
#
#     # Instead of storing (node, path), we store (node, current_number)
#     # The current_number at root is just root.val
#     stack = [(root, root.val)]
#     total_sum = 0
#
#     while stack:
#         node, current_number = stack.pop()
#
#         # Check if we're at a leaf node
#         if not node.left and not node.right:
#             # We've found a complete path, add its number to total
#             total_sum += current_number
#
#         # For each child, the new number is: current_number * 10 + child.val
#         if node.right:
#             stack.append((node.right, current_number * 10 + node.right.val))
#         if node.left:
#             stack.append((node.left, current_number * 10 + node.left.val))
#
#     return total_sum

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(9)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(9)
    print("Path sum: " + str(sol.findSumOfPathNumbers(root)))