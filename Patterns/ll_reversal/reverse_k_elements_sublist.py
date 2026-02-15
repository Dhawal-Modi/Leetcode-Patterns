class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next


class Solution:
    def reverse(self, head, k):

        current, previous = head, None

        while True:
            last_node_of_first_part = previous
            last_node_of_sublist = current
            next = None

            i = 0
            while current is not None and i < k:
                next = current.next
                current.next = previous
                previous = current
                current = next
                i += 1

            if last_node_of_first_part is not None:
                last_node_of_first_part.next = previous  # previous is now the first node of the reversed sublist
            else:
                head = previous

            last_node_of_sublist.next = current

            if current is None:
                break
            previous = last_node_of_sublist
        return head


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

    result = sol.reverse(head, 2)

    print("Nodes of reversed linkedlist are: ", end='')
    print_list(result)


if __name__ == "__main__":
    main()
