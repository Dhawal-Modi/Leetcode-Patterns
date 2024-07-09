class Solution:
    def isValid(self, s):
        stack = []
        for i in range(len(s)):
            if s[i] in ['(', '[', '{']:
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False

                top = stack.pop()

                if s[i] == ')' and top != '(':
                    return False
                if s[i] == ']' and top != '[':
                    return False
                if s[i] == '}' and top != '{':
                    return False

        if len(stack) == 0:
            return True
        return False


if __name__ == "__main__":
    sol = Solution()

    print(sol.isValid('{[()]}'))
    print(sol.isValid('{[}]'))
    print(sol.isValid('(]'))
