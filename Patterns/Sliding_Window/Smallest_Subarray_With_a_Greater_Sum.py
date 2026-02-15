import math


def findMaxSumSubArray(s, arr):
    windowSum, windowStart = 0, 0
    min_len = math.inf
    for windowEnd in range(0,len(arr)):
        windowSum += arr[windowEnd]
        while windowSum >= s:
            min_len = min(windowEnd - windowStart + 1, min_len)
            windowSum -= arr[windowStart]
            windowStart += 1
    if min_len == math.inf:
        return 0
    return min_len



if __name__ == "__main__":
    print(findMaxSumSubArray(7, [2, 1, 5, 2, 3, 2]))
    print(findMaxSumSubArray(7, [2, 1, 5, 2, 8]))
    print(findMaxSumSubArray(8, [3, 4, 1, 1, 6]))
