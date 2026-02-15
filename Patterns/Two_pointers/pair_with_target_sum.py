def search(arr, target_sum):
    # TODO: Write your code here
    first_pointer = 0
    second_pointer = len(arr) - 1

    if len(arr) == 0:
      return [-1, -1]
    while first_pointer != second_pointer :
      s = arr[first_pointer] + arr[second_pointer]
      if s < target_sum:
        first_pointer += 1
      elif s > target_sum:
        second_pointer -= 1
      elif s == target_sum:
        return [first_pointer,second_pointer]
      else:
        return [-1, -1]

if __name__ == "__main__":
    search([1, 2, 3, 4, 6],6)