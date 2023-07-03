class Node:
    def __init__(self, val, next=None):
        self.data = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self, head):
        temp = head
        while temp:
            print(temp.data, end =" ")
            temp = temp.next
        print()

def rotate(head: Node, k: int) -> Node:
    n = 1
    temp = head
    while temp.next:
        n += 1
        temp = temp.next

    k = k % n 
    temp.next = head
    end = n - k
    while end:
        temp = temp.next
        end -= 1
    head = temp.next
    temp.next = None
    return head

if __name__ == '__main__':
     #list1
    head = Node(1);
    head.next = Node(2);
    head.next.next = Node(3);
    head.next.next.next = Node(4);
    head.next.next.next.next = Node(5);
    head.next.next.next.next.next = Node(6);
    head.next.next.next.next.next.next = Node(7);
    k = 2
    
    L = LinkedList()
    LHead = rotate(head, k)
    L.printList(LHead)
