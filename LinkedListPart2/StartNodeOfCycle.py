class Node:
     def __init__(self, data = 0, next = None) -> None:
          self.data = data
          self.next = next

def firstNode(head):
    if head is None:
        return None
        
    slow = head
    fast = head
    isCycle = False

    # Detect if cycle is present
    while fast.next and fast.next.next:        
        slow = slow.next
        fast = fast.next.next 
        if slow == fast:
            isCycle = True
            break

    # If cycle is present, point fast pointer to head keeping slow pointer at it's place 
    # and move both pointers by one step at a time.
    # if fast and slow meets at a point, then this is the start of loop
    if isCycle:
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next

        return slow
    
    return None

if __name__ == '__main__':
     #list1
    head = Node(1);
    head.next = Node(2);
    head.next.next = Node(3);
    head.next.next.next = Node(4);
    head.next.next.next.next = Node(5);
    head.next.next.next.next.next = Node(6);
    head.next.next.next.next.next.next = Node(7);
    head.next.next.next.next.next.next.next = head.next.next.next

    start = firstNode(head)
    if start is not None:
        print("The first node of loop is ", start.data)
    else:
        print("No loop is present in Linked List")