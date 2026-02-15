def find_numbers(nums):
    missing_numbers = []
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
            missing_numbers.append(i + 1)
    return missing_numbers


if __name__ == "__main__":
    print(find_numbers([2, 3, 1, 8, 2, 3, 5, 1]))
    print(find_numbers([1, 1]))
