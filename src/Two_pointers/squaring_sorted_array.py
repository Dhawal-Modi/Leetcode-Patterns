def makeSquares(arr):
    n = len(arr)
    squares = [0 for x in range(n)]
    # TODO: Write your code here
    # for i, ele in enumerate(arr):
    #     ele = ele * ele
    #     squares.pop(i)
    #     squares.insert(i, ele)
    # squares.sort()

    left_pointer = 0
    right_pointer = n - 1
    highestSqIdx = n - 1

    while left_pointer < right_pointer:
        lSq = arr[left_pointer] * arr[left_pointer]
        rSq = arr[right_pointer] * arr[right_pointer]
        if lSq < rSq:
            squares.pop(highestSqIdx)
            squares.insert(highestSqIdx, rSq)
            highestSqIdx -= 1
            right_pointer -= 1
        else:
            squares.pop(highestSqIdx)
            squares.insert(highestSqIdx, lSq)
            highestSqIdx -= 1
            left_pointer += 1
    return squares

if __name__ == "__main__":
    print(makeSquares([-3, -1, 0, 1, 2]))
