class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def dfs(self, node, seq, index):
        if node.val != seq[index]:
            return False

        if index == len(seq) - 1:
            return not node.left and not node.right

        if node.left:
            if self.dfs(node.left,seq, index + 1):
                return True

        if node.right:
            if self.dfs(node.right, seq, index + 1):
                return True

        return False
    def findPath(self, root, sequence):
        idx = 0

        if self.dfs(root,sequence,idx):
            return True
        else:
            return False




if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(9)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(9)
    seq = [1,9,9]
    print(sol.findPath(root,seq))