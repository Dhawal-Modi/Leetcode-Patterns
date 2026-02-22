from collections import defaultdict
from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    num_freq = defaultdict(int)
    for i in nums:
        num_freq[i] += 1

    sorted_num_freq = sorted(num_freq.items(), key=lambda item: item[1], reverse=True)[:k]
    result = []
    for key, val in sorted_num_freq:
        result.append(key)
    return result



if __name__ == "__main__":
    print(topKFrequent(nums = [1,1,1,2,2,3], k = 2))
    print(topKFrequent(nums = [1], k = 1))
    print(topKFrequent(nums = [1,2,1,2,1,2,3,1,3,2], k = 2))