import math


def sort(arr):
    # TODO: Write your code here
    lo = 0
    hi = len(arr) - 1

    while arr[lo] <= arr[lo + 1] and lo < len(arr) - 1:
        lo += 1

    if lo == len(arr) - 1:
        return 0

    while arr[hi] >= arr[hi - 1] and hi > 0:
        hi -= 1

    # sub_max = -math.inf
    # sub_min = math.inf
    # for k in range(lo,hi+1):
    #     sub_max = max(arr[k], sub_max)
    #     sub_min = min(arr[k], sub_min)

    sub_max = max(arr[lo:hi + 1])
    sub_min = min(arr[lo:hi + 1])

    while lo > 0 and arr[lo - 1] > sub_min:
        lo -= 1

    while hi < len(arr) - 1 and arr[hi + 1] < sub_max:
        hi += 1

    return hi - lo + 1


if __name__ == "__main__":
    print(sort([1, 2, 5, 3, 7, 10, 9, 12]))
    print(sort([1, 3, 2, 0, -1, 7, 10]))
    print(sort([2,6,4,8,10,9,15]))
