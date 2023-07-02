class Node:
     def __init__(self, data = 0, next = None) -> None:
          self.data = data
          self.next = next

def hasCycle(head):
    if head is None:
            return False  
    p1 = head
    p2 = head

    while p2.next and p2.next.next:        
        p1 = p1.next
        p2 = p2.next.next 
        if p1 == p2:
            return True

    return False

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

    if hasCycle(head):
         print("The given linked list have cycle")
    else:
         print("The given linked list does not have a cycle")



