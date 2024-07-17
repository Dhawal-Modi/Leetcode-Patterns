class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        sl = list(s)
        for current_letter_idx in range(len(sl)):
            if stack and stack[-1] == sl[current_letter_idx]:
                stack.pop()
            else:
                stack.append(sl[current_letter_idx])
        return ''.join(stack)


def main():
    sol = Solution()

    result = sol.removeDuplicates("fooobar")
    result1 = sol.removeDuplicates("abbaca")
    print(result)
    print(result1)


if __name__ == "__main__":
    main()
