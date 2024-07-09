class Solution:
    def sortStack(self, stack):
        tempStack = []

        while stack:
            tmp = stack.pop()

            while tempStack and tempStack[-1] > tmp:
                stack.append(tempStack.pop())
            tempStack.append(tmp)
        return tempStack


if __name__ == "__main__":
    sol = Solution()

    print(sol.sortStack([34, 3, 31, 98, 92, 23]))
    print(sol.sortStack([4, 3, 2, 10, 12, 1, 5, 6]))
    print(sol.sortStack([20, 10, -5, -1]))
