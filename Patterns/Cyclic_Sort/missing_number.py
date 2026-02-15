def find_missing_number(nums):
    n = len(nums)
    i = 0
    while i < n:
        j = nums[i]
        if nums[i] < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(n):
        if nums[i] != i:
            return i
    return n


if __name__ == "__main__":
    print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))
