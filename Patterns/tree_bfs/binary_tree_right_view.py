from pydantic.validators import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def traverse(self, root):
        result = [] # List[int]

        q = deque()
        q.append(root)

        while q:
            level_size = len(q)
            current_level = []

            for _ in range(level_size):
                current_node = q.popleft()
                current_val = current_node.val

                current_level.append(current_val)

                if current_node.left:
                    q.append(current_node.left)

                if current_node.right:
                    q.append(current_node.right)

            result.append(current_level[-1])

        return result

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print("Level order traversal: " + str(sol.traverse(root)))