class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for letter in s:
            if stack and stack[-1][0] == letter:
                stack[-1][1] += 1
            else:
                stack.append([letter, 1])
            if stack[-1][1] == k:
                stack.pop()


        return ''.join(letter * n for letter,n in stack)


def main():
    sol = Solution()

    result = sol.removeDuplicates("abbbaaca", k=3)
    result1 = sol.removeDuplicates("abbaccaa", k=3)
    result2 = sol.removeDuplicates("abbacccaa", k=3)
    print(result)
    print(result1)
    print(result2)


if __name__ == "__main__":
    main()
