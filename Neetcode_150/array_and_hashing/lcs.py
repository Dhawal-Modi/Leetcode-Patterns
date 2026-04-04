from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        if len(num_set) == 0:
            return 0

        best = 0
        for num in num_set:
            # num - 1 is key idea to identify start of subsequence if num - 1
            # dont exist in set then num is start of a subsequence
            if int(num-1) not in num_set:
                length = 0
                current = num
                while current in num_set:
                    current += 1
                    length += 1

                best = max(best,length)

        return best




if __name__ == "__main__":
    sol = Solution()
    print(sol.longestConsecutive(nums=[100,4,200,1,3,2]))
    print(sol.longestConsecutive(nums=[0,3,7,2,5,8,4,6,0,1]))
    print(sol.longestConsecutive(nums=[1,0,1,2]))