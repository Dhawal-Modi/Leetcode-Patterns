from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def traverse(self, root):
        result = []

        q = deque()
        q.append(root)
        lr = True
        while q:
            levelsize = len(q)
            currentlevel = deque()
            for i in range(levelsize):
                current_node = q.popleft()
                current_val = current_node.val

                if lr:
                    currentlevel.append(current_val)
                else:
                    currentlevel.appendleft(current_val)

                if current_node.left:
                    q.append(current_node.left)

                if current_node.right:
                    q.append(current_node.right)


            result.append(list(currentlevel))
            lr = not lr

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