class Node:
  def __init__(self, value, next=None):
    self.val = value
    self.next = next


class Solution:
  def hasCycle(self, head):
    slow, fast = head, head
    while fast is not None and fast.next is not None:
      fast = fast.next.next  # Move fast pointer two steps at a time
      slow = slow.next      # Move slow pointer one step at a time
      if slow == fast:      # Check if slow and fast pointers meet (cycle detected)
        return True         # Found a cycle in the linked list
    return False            # No cycle found in the linked list

def main():
  sol = Solution()
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  print("LinkedList has cycle: " + str(sol.hasCycle(head)))

  head.next.next.next.next.next.next = head.next.next
  print("LinkedList has cycle: " + str(sol.hasCycle(head)))

  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList has cycle: " + str(sol.hasCycle(head)))

main()
