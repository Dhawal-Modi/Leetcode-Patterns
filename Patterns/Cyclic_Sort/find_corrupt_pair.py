def find_numbers(nums):
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
            return [nums[i], i + 1]
    return [-1, -1]


if __name__ == "__main__":
    print(find_numbers([3, 1, 2, 5, 2]))
    print(find_numbers([3, 1, 2, 3, 6, 4]))
