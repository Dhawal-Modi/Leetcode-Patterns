def findSubstring(str1, pattern):
    window_start, matched, substr_start = 0,0,0
    char_map = {}
    min_len = len(str1) + 1

    for chr in pattern:
        if chr not in char_map:
            char_map[chr] = 0
        char_map[chr] += 1

    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char in char_map:
            char_map[right_char] -= 1
            if char_map[right_char] >= 0:
                matched += 1

        while matched == len(pattern):
            if min_len > window_end - window_start + 1:
                min_len = window_end - window_start + 1
                substr_start = window_start

            left_char = str1[window_start]
            window_start += 1
            if left_char in char_map:
                if char_map[left_char] == 0:
                    matched -= 1
                char_map[left_char] += 1

    if min_len > len(str1):
        return ""
    return str1[substr_start:substr_start + min_len]


if __name__ == "__main__":
    print(findSubstring("aabdec", "abc"))
    print(findSubstring("aabdec", "abac"))