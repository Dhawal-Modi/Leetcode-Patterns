def find_number(nums):
    n = len(nums)
    i = 0

    while i < n:
        j = nums[i] - 1
        if 0 < nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return len(nums) + 1


if __name__ == "__main__":
    print(find_number([-3, 1, 5, 4, 2]))
    print(find_number([3, -2, 0, 1, 2]))
    print(find_number([3, 2, 5, 1]))
