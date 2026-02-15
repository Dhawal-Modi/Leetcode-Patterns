def findLength(fruits, k):
    max_length = 0
    window_start = 0
    char_map = {}

    for window_end in range(len(fruits)):
        right_char = fruits[window_end]
        if right_char not in char_map:
            char_map[right_char] = 0
        char_map[right_char] += 1

        while len(char_map) > k:
            left_char = fruits[window_start]
            char_map[left_char] -= 1
            if char_map[left_char] == 0:
                del char_map[left_char]
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


if __name__ == "__main__":
    print(findLength(['A', 'B', 'C', 'A', 'C'], 2))
    print(findLength(['A', 'B', 'C', 'B', 'B', 'C'], 2))