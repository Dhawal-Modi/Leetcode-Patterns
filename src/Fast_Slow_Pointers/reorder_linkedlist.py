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

        reversed_second_half = self.reverseL(slow)
        first_half = head


        while first_half is not None and reversed_second_half is not None:
            tmp = first_half.next
            first_half.next = reversed_second_half
            first_half = tmp

            tmp = reversed_second_half.next
            reversed_second_half.next = first_half
            reversed_second_half = tmp

        if first_half is not None:
            first_half.next = None
        return head



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
