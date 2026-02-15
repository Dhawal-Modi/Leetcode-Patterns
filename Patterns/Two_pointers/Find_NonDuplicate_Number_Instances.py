def remove(arr):
    if len(arr) == 0:
        return 0

    first_pointer = 0
    second_pointer = 1

    while first_pointer < len(arr):
        if (arr[second_pointer - 1] != arr[first_pointer]):
            arr[second_pointer] = arr[first_pointer]
            second_pointer += 1
        first_pointer += 1
    return second_pointer

if __name__ == "__main__":
    print(remove([0,0,1,1,1,2,2,3,3,4]))
