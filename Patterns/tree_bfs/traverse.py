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

        while q:
            levelsize = len(q)
            currentlevel = []
            for i in range(levelsize):
                currentnode = q.popleft()
                currentval = currentnode.val

                currentlevel.append(currentval)

                if currentnode.left:
                    q.append(currentnode.left)

                if currentnode.right:
                    q.append(currentnode.right)

            result.append(currentlevel)

        return result

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: " + str(sol.traverse(root)))