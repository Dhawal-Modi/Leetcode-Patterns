def findNumbers(nums, k):
    missingNumbers = []
    n = len(nums)
    i = 0

    while i < n:
        j = nums[i] - 1
        if 0 < nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    extra_numbers = set()
    for i in range(n):
        if len(extra_numbers) < k and nums[i] != i + 1:
            missingNumbers.append(i + 1)
            extra_numbers.add(nums[i])

    current = n + 1
    while len(missingNumbers) < k:
        if current not in extra_numbers:
            missingNumbers.append(current)
        current += 1
    return missingNumbers


if __name__ == "__main__":
    print(findNumbers([3, -1, 4, 5, 5], 3))
    print(findNumbers([2, 3, 4], 3))
