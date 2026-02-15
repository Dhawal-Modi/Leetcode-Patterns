class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next


class Solution:
    def rotate(self, head, rotations):

        last_node = head
        length = 1
        while last_node.next is not None:
            last_node = last_node.next
            length += 1

        rotations = rotations % length
        if rotations == 0:
            return head

        last_node.next = head

        steps_end = length - rotations
        new_end = head
        for i in range(steps_end - 1):
            new_end = new_end.next

        new_head = new_end.next
        new_end.next = None

        return new_head


def print_list(head):
    temp = head
    while temp is not None:
        print(temp.val, end=" ")  # Use temp.val to access the value
        temp = temp.next
    print()


def main():
    sol = Solution()
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    print("Nodes of original linkedlist are: ", end='')
    print_list(head)

    result = sol.rotate(head, 2)

    print("Nodes of reversed linkedlist are: ", end='')
    print_list(result)


if __name__ == "__main__":
    main()
