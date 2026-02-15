def searchTriplet(arr):
    triplets = []
    left = 0
    arr.sort()

    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        searchPair(arr, -arr[i], i + 1, triplets)
    return triplets


def searchPair(arr, targetSum, left, triplets):
    right = len(arr) - 1
    while (left < right):
        currentSum = arr[right] + arr[left]
        if currentSum == targetSum:
            triplets.append([-arr[targetSum], arr[right], arr[left]])
            left += 1
            right -= 1
            while (left < right) and (arr[left] == arr[left - 1]):
                left += 1
            while (left < right) and (arr[right] == arr[right + 1]):
                right -= 1
        elif (targetSum > currentSum):
            left += 1
        elif (targetSum < currentSum):
            right -= 1

if __name__ == "__main__":
    print(searchTriplet([-3, 0, 1, 2, -1, 1, -2]))
