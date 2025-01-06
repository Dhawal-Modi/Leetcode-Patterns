from _collections import OrderedDict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 0:
            return -1


        ordd = OrderedDict.fromkeys(s,0)
        for c in s:
            ordd[c] += 1

        for i,(k,v) in enumerate(ordd.items()):
            if v == 1:
                return s.index(k)
        return -1

sol = Solution()
res = sol.firstUniqChar("abcab")
print(res)

res1 = sol.firstUniqChar("apple")
print(res1)

res2 = sol.firstUniqChar("abab")
print(res2)