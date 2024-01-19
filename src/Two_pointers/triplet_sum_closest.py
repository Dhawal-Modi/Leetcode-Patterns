import math


def searchTriplet(arr, target_sum):

    arr.sort()
    smallest_diff = math.inf
    for i in range(len(arr)-2):
        left = i + 1
        right = len(arr) - 1
        while left < right:
            target_diff = target_sum - arr[i] - arr[left] - arr[right]
            if target_diff == 0:
                return target_sum
            if abs(target_diff) < abs(smallest_diff) or (abs(target_diff) == abs(smallest_diff) and (target_diff) > abs(smallest_diff)):
                smallest_diff = target_diff
            if target_diff > 0:
                left += 1
            else:
                right -= 1
    return target_sum - smallest_diff


if __name__ == "__main__":
    print(searchTriplet([-1, 0, 2, 3], 3))
