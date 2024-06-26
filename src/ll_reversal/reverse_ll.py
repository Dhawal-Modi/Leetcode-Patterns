class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next


class Solution:
    def reverse(self, head):
        result = None
        prev, current, next = None, head, None
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next

        return prev


def print_list(head):
    temp = head
    while temp is not None:
        print(temp.val, end=" ")  # Use temp.val to access the value
        temp = temp.next
    print()


def main():
    sol = Solution()
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)

    print("Nodes of original linkedlist are: ", end='')
    print_list(head)
    result = sol.reverse(head)
    print("Nodes of reversed linkedlist are: ", end='')
    print_list(result)


if __name__ == "__main__":
    main()
