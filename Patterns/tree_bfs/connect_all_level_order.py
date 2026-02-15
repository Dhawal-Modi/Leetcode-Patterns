from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right, self.next = None, None, None


class Solution:
    def connect(self, root):
        if root is None:
            return []

        q = deque()
        q.append(root)

        prev_node = None
        current_node = None
        while q:

            current_node = q.popleft()

            if prev_node:
                prev_node.next = current_node

            prev_node = current_node

            if current_node.left:
                q.append(current_node.left)

            if current_node.right:
                q.append(current_node.right)

        return root

# tree traversal using 'next' pointer
def print_tree(node):
    print("Traversal using 'next' pointer: ", end='')
    current = node
    while current:
        print(str(current.val) + " ", end='')
        current = current.next
    print()

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    sol.connect(root)
    print_tree(root)