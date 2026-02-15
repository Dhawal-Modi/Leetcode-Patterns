from collections import defaultdict

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        min_count = float('inf')

        str_dict = defaultdict(int)
        ballon_dict = {'b':1,'a':1,'l':2,'o':2,'n':1}

        for i in text:
            if i not in str_dict:
                str_dict[i] = 1
            else:
                str_dict[i] += 1

        min_count = min(min_count,str_dict['b'])
        min_count = min(min_count,str_dict['a'])
        min_count = min(min_count,str_dict['l']//2)
        min_count = min(min_count,str_dict['o']//2)
        min_count = min(min_count,str_dict['n'])

        return min_count

sol = Solution()
res = sol.maxNumberOfBalloons("balloonballoon")
res1 = sol.maxNumberOfBalloons("bbaall")
res2 = sol.maxNumberOfBalloons("balloonballoooon")
print(res)
print(res1)
print(res2)