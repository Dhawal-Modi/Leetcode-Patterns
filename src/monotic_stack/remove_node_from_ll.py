class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNodes(self, head):
        current = head
        stack = []
        while current is not None:
            while stack and stack[-1].val < current.val:
                stack.pop()
            if stack:
                stack[-1].next = current
            stack.append(current)
            current = current.next

        return stack[0] if stack else None


def print_list(head):
    temp = head
    while temp is not None:
        print(temp.val, end=" ")  # Use temp.val to access the value
        temp = temp.next
    print()


def main():
    sol = Solution()
    head = ListNode(5)
    head.next = ListNode(3)
    head.next.next = ListNode(7)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(2)
    head.next.next.next.next.next = ListNode(1)

    print("Nodes of original linkedlist are: ", end='')
    print_list(head)

    result = sol.removeNodes(head)

    print("Nodes of reversed linkedlist are: ", end='')
    print_list(result)


if __name__ == "__main__":
    main()
