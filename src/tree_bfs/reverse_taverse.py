from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def traverse(self, root):
        result = deque()

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

            result.appendleft(currentlevel)

        result = [list(sublist) for sublist in result]
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