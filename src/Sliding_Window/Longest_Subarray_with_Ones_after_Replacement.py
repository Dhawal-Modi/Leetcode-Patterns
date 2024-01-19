def findLength(nums, k):
    max_length, window_start, max_repeat_count = 0, 0, 0
    

    for window_end in range(len(nums)):
        if nums[window_end] == 1:
            max_repeat_count += 1

        if (window_end - window_start + 1) - max_repeat_count > k:
            if nums[window_start] == 1:
                max_repeat_count -= 1
            window_start += 1

        max_length = max(window_end - window_start + 1, max_length)
    return max_length


if __name__ == "__main__":
    print(findLength([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
    print(findLength([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))
    #print(findLength("abccde", 1))