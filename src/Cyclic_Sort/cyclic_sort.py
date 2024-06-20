def sort(arr):
    i = 0
    while i < len(arr):
        j = arr[i] - 1
        if arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1


if __name__ == "__main__":
    print(sort([2, 6, 4, 3, 1, 5]))
