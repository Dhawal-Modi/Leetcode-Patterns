class Solution:
    def nextGreaterElement(self, nums1, nums2):

        stack = []
        next_greater = {}

        for i in reversed(nums2):
            while stack and stack[-1] <= i:
                stack.pop()
            if stack:
                next_greater[i] = stack[-1]
            stack.append(i)

        return [next_greater.get(num, -1) for num in nums1]


def main():
    sol = Solution()

    result = sol.nextGreaterElement([4, 2, 6], [6, 2, 4, 5, 3, 7])
    result1 = sol.nextGreaterElement([5, 12, 3], [12, 3, 5, 4, 10, 15])
    print(result)
    print(result1)


if __name__ == "__main__":
    main()
