# def searchTriplets(arr, target):
#     count = 0
#     arr.sort()
#
#     for i in range(len(arr) - 2):
#         count += searchPair(arr, target - arr[i], i)
#     return count
#
# def searchPair(arr, t, idx):
#     count = 0
#     left = idx + 1
#     right = len(arr) - 1
#     while left < right:
#         current_sum = arr[left] + arr[right]
#         if current_sum < t:
#             count += right - left
#             left += 1
#         else:
#             right -= 1
#     return count

def search_triplets(arr, target):
    arr.sort()  # Sort the array
    count = 0

    for i in range(len(arr) - 2):
        left, right = i + 1, len(arr) - 1

        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]

            # If the sum is less than the target, all elements between left and right
            # can form a triplet with arr[i], as the array is sorted
            if current_sum < target:
                count += (right - left)
                left += 1  # Move the left pointer to check for other pairs
            else:
                right -= 1  # Reduce the sum by moving the right pointer

    return count

if __name__ == "__main__":
    print(search_triplets([-1, 4, 2, 1, 3],5))
    print(search_triplets([-1, 0, 2, 3], 3))