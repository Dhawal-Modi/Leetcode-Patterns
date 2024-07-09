class Solution:
    def decimalToBinary(self, num):
        stack = []
        s = ''
        while num != 0:
            remainder = num % 2
            num = num // 2

            stack.append(str(remainder))

        while len(stack) != 0:
            top = stack.pop()
            s += top

        return s


if __name__ == "__main__":
    sol = Solution()

    print(sol.decimalToBinary(2))
    print(sol.decimalToBinary(7))
    print(sol.decimalToBinary(18))
