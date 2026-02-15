def findStringAnagrams(str1, pattern):
    window_start,matched =0,0
    char_map = {}

    for chr in pattern:
        if chr not in char_map:
            char_map[chr] = 0
        char_map[chr] += 1

    result_indices = []
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char in char_map:
            char_map[right_char] -= 1
            if char_map[right_char] == 0:
                matched += 1

        if matched == len(char_map):
            result_indices.append(window_start)

        if window_end >= len(pattern) - 1:
            left_char = str1[window_start]
            window_start += 1
            if left_char in char_map:
                if char_map[left_char] == 0:
                    matched -= 1
                char_map[left_char] += 1
    return result_indices


if __name__ == "__main__":
    print(findStringAnagrams("ppqp", "pq"))
    print(findStringAnagrams("abbcabc", "abc"))