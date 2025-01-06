def longest_palindrome(inp_string):
    letter_dict = {}
    length = 0

    for letter in inp_string:
        if letter not in letter_dict:
            letter_dict[letter] = 0
        letter_dict[letter] += 1

    flag = 0
    for k,v in letter_dict.items():
        if v % 2 == 0:
            length += v
        elif v % 2 != 0:
            length += v - 1
            flag = 1

    if flag == 1:
        length += 1

    return length


if __name__ == "__main__":
    #input_string = input()

    test_case1 = "applepie"
    test_case2 = "aabbcc"
    test_case3 = "bananas"

    print(longest_palindrome(test_case1))
    print(longest_palindrome(test_case2))
    print(longest_palindrome(test_case3))

