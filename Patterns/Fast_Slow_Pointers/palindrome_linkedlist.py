class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next


class Solution:
    def isPalindrome(self, head):
        slow, fast = head, head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        reversed_half = self.reverseL(slow)
        copy_reversed_half = reversed_half

        while head is not None and reversed_half is not None:
            if head.val != reversed_half.val:
                break
            head = head.next
            reversed_half = reversed_half.next

        self.reverseL(copy_reversed_half)

        if head is None or reversed_half is None:
            return True
        return False

    def reverseL(self, head):
        current = head
        prev = None

        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev


def main():
    sol = Solution()
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)

    print("Is palindrome: " + str(sol.isPalindrome(head)))

    head.next.next.next.next.next = Node(2)
    print("Is palindrome: " + str(sol.isPalindrome(head)))


main()
