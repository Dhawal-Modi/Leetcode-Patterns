class Solution:
    def dailyTemperatures(self, temperatures):
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)

        return res


def main():
    sol = Solution()

    result = sol.dailyTemperatures([70, 73, 75, 71, 69, 72, 76, 73])
    result1 = sol.dailyTemperatures([73, 72, 71, 70])
    print(result)
    print(result1)


if __name__ == "__main__":
    main()