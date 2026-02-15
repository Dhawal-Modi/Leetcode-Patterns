from collections import deque

class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = self.right = self.next = None

class Solution:
    def connect(self, root):
        if not root:
            return None

        q = deque()
        q.append(root)

        while q:
            prev_node = None
            level_size = len(q)

            for _ in range(level_size):
                current_node = q.popleft()

                # Need to actually connect the nodes using 'next'. Just collecting values won't work
                if prev_node:
                    prev_node.next = current_node

                prev_node = current_node

                if current_node.left:
                    q.append(current_node.left)

                if current_node.right:
                    q.append(current_node.right)

            if prev_node:
                prev_node.next = None

        return root



if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print("Level order traversal: " + str(sol.connect(root)))

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: " + str(sol.connect(root)))

