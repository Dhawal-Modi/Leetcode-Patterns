class Solution:
    def reverseString(self, s):
        stack = []
        ns = ''
        for i in range(len(s)):
            stack.append(s[i])

        while len(stack) != 0:
            top = stack.pop()

            ns += top

        return ns


if __name__ == "__main__":
    sol = Solution()

    print(sol.reverseString("Hello, World!"))
    print(sol.reverseString("OpenAI"))
    print(sol.reverseString("Stacks are fun!"))
