def dnp(arr):
    left = 0
    right = len(arr) - 1
    i = 0
    while i <= right:
        if arr[i] == 0:
            arr[left], arr[i] = arr[i], arr[left]
            left += 1
            i+= 1
        elif arr[i] == 1:
            i += 1
        elif arr[i] == 2:
            arr[right], arr[i] = arr[i], arr[right]
            right -= 1

    return arr

if __name__ == "__main__":
    print(dnp([2, 2, 0, 1, 2, 0]))