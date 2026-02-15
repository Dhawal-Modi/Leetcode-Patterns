def find(num):
    slow, fast = num,num
    while True:
        slow = sq_sum(slow)
        fast = sq_sum(sq_sum(fast))
        if slow == fast:
            break
    return slow == 1


def sq_sum(num):
    square_sum = 0
    while num > 0:
        digit = num % 10
        square_sum += digit * digit
        num //= 10
    return square_sum

if __name__ == "__main__":
    print(find(23))
