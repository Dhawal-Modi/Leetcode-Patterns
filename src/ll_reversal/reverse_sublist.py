class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next


class Solution:
    def reverse(self, head, p, q):
        if p == q:
            return head

        current, previous = head, None
        i = 0

        # Step 1: Skip the first p-1 nodes
        while current is not None and i < p - 1:
            previous = current
            current = current.next
            i += 1

        # We are interested in three parts of the LinkedList, the part before index p,
        # the part between p and q, and the part after index q
        last_node_of_first_part = previous  # node at index p-1
        last_node_of_sublist = current  # node at index p
        next = None  # will be used to temporarily store the next node

        # Step 2: Reverse nodes between p and q
        i = 0
        while current is not None and i < q - p + 1:
            next = current.next
            current.next = previous
            previous = current
            current = next
            i += 1

        # Step 3: Connect with the first part
        if last_node_of_first_part is not None:
            last_node_of_first_part.next = previous  # previous is now the first node of the reversed sublist
        else:
            head = previous

        # Step 4: Connect with the last part
        last_node_of_sublist.next = current

        return head


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
    result = sol.reverse(head, 2, 4)
    print("Nodes of reversed linkedlist are: ", end='')
    print_list(result)


if __name__ == "__main__":
    main()
