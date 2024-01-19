def find_subarrays(arr, target):
    result = []
    # TODO: Write your code here\
    product = 1
    first_pointer, second_pointer = 0, 0

    for second_pointer in range(len(arr)):
        product = product * arr[second_pointer]

        while product >= target and first_pointer <= second_pointer:
            product /= arr[first_pointer]
            first_pointer += 1

        temp_list = []
        for i in range(second_pointer, first_pointer -1,-1):
            temp_list.insert(0,arr[i])
            result.append(list(temp_list))

    return result

if __name__ == "__main__":
    print(find_subarrays([2, 5, 3, 10],30))