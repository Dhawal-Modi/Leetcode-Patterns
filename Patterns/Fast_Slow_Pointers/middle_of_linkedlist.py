class Node:
  def __init__(self, value, next=None):
    self.val = value
    self.next = next

# Function to find the middle of a linked list
def findMiddle(head):
    slow = head
    fast = head

    # Traverse the linked list with two pointers (slow and fast)
    # until the fast pointer reaches the end or goes one step further
    while (fast is not None and fast.next is not None):
        slow = slow.next
        fast = fast.next.next

    # Return the node pointed to by the slow pointer, which is the middle
    return slow


# Main function to test the findMiddle function
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
