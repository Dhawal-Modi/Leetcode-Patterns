# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cl = 0
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                cl = self.findLength(slow)
                break
        else:
            return None

        pointer1 = head
        pointer2 = head

        while cl > 0:
            pointer2 = pointer2.next
            cl -= 1

        while pointer1 != pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next

        return pointer1         

    def findLength(self, slow: Optional[ListNode]) -> int:
        l = 0
        current = slow

        while True:
            current = current.next
            l += 1
            if current == slow:
                break

        return l

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    # Print the middle node's value
    print("Middle Node: " + str(findMiddle(head).val))

    head.next.next.next.next.next = Node(6)
    # Print the middle node's value after adding a new node
    print("Middle Node: " + str(findMiddle(head).val))

    head.next.next.next.next.next.next = Node(7)
    # Print the middle node's value after adding another new node
    print("Middle Node: " + str(findMiddle(head).val))


# Call the main function to execute the code
main()