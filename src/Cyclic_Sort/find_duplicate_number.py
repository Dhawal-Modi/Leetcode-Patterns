def find_number(nums):
    n = len(nums)
    i = 0

    while i < n:
        if nums[i] != i + 1:
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                return nums[i]
        else:
            i += 1

    return -1


if __name__ == "__main__":
    print(find_number([1, 4, 4, 3, 2]))
    print(find_number([2, 1, 3, 3, 5, 4]))
    print(find_number([2, 4, 1, 4, 4]))
