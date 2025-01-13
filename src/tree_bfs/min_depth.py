from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def findDepth(self, root):
        minimumTreeDepth = 0


        q = deque()
        q.append(root)

        while q:
            current_level = []
            level_size = len(q)
            minimumTreeDepth += 1
            for _ in range(level_size):

                current_node = q.popleft()
                current_val = current_node.val

                current_level.append(current_val)

                if not current_node.left and not current_node.right:
                    return minimumTreeDepth

                if current_node.left:
                    q.append(current_node.left)

                if current_node.right:
                    q.append(current_node.right)

        return minimumTreeDepth

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print("Level order traversal: " + str(sol.findDepth(root)))
