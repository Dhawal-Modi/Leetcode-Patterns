class Solution:
    def nextLargerElement(self, arr):
        res = [-1] * len(arr)
        stack = []

        for i in range(2 * len(arr)):
            while len(stack) != 0 and arr[stack[-1]] < (arr[i % len(arr)]):
                res[stack.pop()] = arr[i % len(arr)]

            if i < len(arr):
                stack.append(i)
        return res


if __name__ == "__main__":
    sol = Solution()

    print(sol.nextLargerElement([1, 2, 3, 4, 3]))

