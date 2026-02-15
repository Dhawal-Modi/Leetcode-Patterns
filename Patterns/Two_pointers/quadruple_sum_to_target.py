def searchQuadruplets(arr, target):
    quadruplets = []

    arr.sort()

    for i in range(len(arr) - 3):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        for j in range(i + 1, len(arr) - 2):
            if j > i + 1 and arr[j] == arr[j - 1]:
                continue

            left, right = j + 1, len(arr) - 1

            while left < right:
                current_sum = arr[i] + arr[j] + arr[left] + arr[right]

                if current_sum == target:
                    quadruplets.append([arr[i], arr[j], arr[left], arr[right]])
                    left += 1
                    right -= 1
                    while left < right and arr[left] == arr[left - 1]:
                        left += 1
                    while right > left and arr[right] == arr[right + 1]:
                        right -= 1
                elif current_sum > target:
                    right -= 1  # Reduce the sum by moving the right pointer
                elif current_sum < target:
                    left += 1

    return quadruplets


if __name__ == "__main__":
    print(searchQuadruplets([4, 1, 2, -1, 1, -3], 1))
