from collections import defaultdict

class Solution:
    def largestUniqueNumber(self, A: list[int]) -> int:
        maxUnique = -1

        num_dict = defaultdict()
        for i in A:
            if i not in num_dict:
                num_dict[i] = 1
            else:
                num_dict[i] += 1

        for k,v in num_dict.items():
            if v == 1 and k >= maxUnique:
                maxUnique = max(k,maxUnique)
                #return maxUnique

        return maxUnique


sol = Solution()
res = sol.largestUniqueNumber([5, 7, 3, 7, 5, 8])
res1 = sol.largestUniqueNumber([1, 2, 3, 2, 1, 4, 4])
res2 = sol.largestUniqueNumber([9, 9, 8, 8, 7, 7])
print(res)
print(res1)
print(res2)