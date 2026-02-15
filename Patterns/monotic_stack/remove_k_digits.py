class Solution:
    def removeKdigits(self, nums: str, k: int):
        stack = []
        for num in nums:
            while stack and stack[-1] > int(num) and k > 0:
                stack.pop()
                k -= 1
            stack.append(int(num))

        if k > 0:
            for i in range(k):
                stack.pop()

        fs = (''.join(str(n) for n in stack)).lstrip('0')
        if fs:
            return fs
        else:
            return "0"


def main():
    sol = Solution()

    result = sol.removeKdigits("1432219", k=3)
    result1 = sol.removeKdigits("10200", k=1)
    result2 = sol.removeKdigits("1901042", k=4)
    result3 = sol.removeKdigits("200500", k=2)
    result4 = sol.removeKdigits("54321", k =5)
    print(result)
    print(result1)
    print(result2)
    print(result3)
    print(result4)


if __name__ == "__main__":
    main()
