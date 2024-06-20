def find_numbers(nums):
    duplicateNumbers = []
    n = len(nums)
    i = 0
    while i < n:
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(n):
        if nums[i] != i + 1:
            duplicateNumbers.append(nums[i])
    return duplicateNumbers


if __name__ == "__main__":
    print(find_numbers([5, 4, 7, 2, 3, 5, 3]))
