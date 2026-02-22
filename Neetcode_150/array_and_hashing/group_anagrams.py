from collections import defaultdict
from email.policy import default
from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    # grouped = {}
    grouped = defaultdict(list)

    for word in strs:
        uniq_chars = ''.join(sorted(word))
        # if uniq_chars not in grouped:
        #     grouped[uniq_chars] = []
        grouped[uniq_chars].append(word)

    return list(grouped.values())

    # result = []
    # for k,v in enumerate(grouped):
    #     result.append(grouped[v])
    # return result

if __name__ == "__main__":
    print(groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(groupAnagrams(strs=[""]))
    print(groupAnagrams(strs=["a"]))
