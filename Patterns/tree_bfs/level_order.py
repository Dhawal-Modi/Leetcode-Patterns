from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def findSuccessor(self, root, key):
        if not root:
            return None

        queue = deque()
        queue.append(root)

        while queue:

            current_node = queue.popleft()
            current_val = current_node.val

            if current_node.left:
                queue.append(current_node.left)

            if current_node.right:
                queue.append(current_node.right)

            if current_val == key:
                return (queue.popleft()).val

        return None

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print("Level order traversal: " + str(sol.findSuccessor(root,3)))

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print("Level order traversal: " + str(sol.findSuccessor(root,1)))

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: " + str(sol.findSuccessor(root,9)))