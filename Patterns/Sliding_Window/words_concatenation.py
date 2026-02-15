def findWordConcatenation(str1, words):
    result_indices = []
    word_map = {}

    for word in words:
        if word not in word_map:
            word_map[word] = 0
        word_map[word] += 1

    words_count = len(words)
    word_length = len(words[0])

    # This for loop iterates over str1 considering every possible starting idx for a substring. We need the last idx
    # calculated by (len(str1) - words_count * word_length + 1) where the concatenation of words can fit in the string.
    # AKA we're calculating the maximum starting idx
    for i in range((len(str1) - words_count * word_length) + 1):
        words_seen = {}
        # The inner loop (indexed by j) iterates over the number of words (words_count), attempting to find each word in
        # sequence within the substring starting at i.
        for j in range(0, words_count):
            next_word_idx = i + j * word_length
            word = str1[next_word_idx:next_word_idx + word_length]

            if word not in word_map:
                break

            if word not in words_seen:
                words_seen[word] = 0
            words_seen[word] += 1

            if words_seen[word] > word_map.get(word, 0):
                break

            # j starts from 0, so when j + 1 equals words_count, it means that the loop has successfully checked for the
            # presence of words_count words in sequence from the current starting point i.
            if j + 1 == words_count:
                result_indices.append(i)

    return result_indices


if __name__ == "__main__":
    print(findWordConcatenation("catfoxcat", ["cat", "fox"]))
