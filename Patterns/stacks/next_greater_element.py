class Solution:
    def nextLargerElement(self, arr):
        res = [-1] * len(arr)
        stack = []

        for i in reversed(arr):
            while len(stack) != 0 and stack[-1] <= i:
                stack.pop()

            if stack:
                res[arr.index(i)] = stack[-1]
            stack.append(i)
        return res


if __name__ == "__main__":
    sol = Solution()

    print(sol.nextLargerElement([4, 5, 2, 25]))
    print(sol.nextLargerElement([13, 7, 6, 12]))
    print(sol.nextLargerElement([1, 2, 3, 4, 5]))
    
