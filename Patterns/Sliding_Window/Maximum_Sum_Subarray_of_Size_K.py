import math


def findMaxSumSubArray(k, arr):
    windowSum, windowStart = 0, 0
    max_sum = -math.inf
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        if windowEnd >= k - 1:
            max_sum = max(windowSum, max_sum)
            windowSum -= arr[windowStart]
            windowStart += 1
    return max_sum


if __name__ == "__main__":
    print(findMaxSumSubArray(3, [2, 1, 5, 1, 3, 2]))
