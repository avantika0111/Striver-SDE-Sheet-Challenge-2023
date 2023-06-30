class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = LinkedListNode(data)
        if self.head is None:
            self.head = node
            return 
        end = self.head
        while end.next:
            end = end.next
        end.next = node

    def printList(self, head):
        temp = head
        while temp:
            print(temp.data, end =" ")
            temp = temp.next
        print()

def removeKthNode(head, k):
    p1 = head
    p2 = head
    for i in range(1, k+1):
        p2 = p2.next

    if p2 is None:
        return p1.next
        
    while p2 is not None:
        prev = p1
        p1 = p1.next
        p2 = p2.next

    if p1.next is None:
        prev.next = None
    else:
        prev.next = p1.next

    return head

if __name__ == '__main__':
    inp = list(map(int, input("Enter Linked List Elements - ").split()))
    k = int(input("Enter index from last to delete - "))
    llist = LinkedList()
    for i in range(len(inp)):
        llist.append(inp[i])

    new_head = removeKthNode(llist.head, k)
    print("Linked List after removing Kth element: ")
    llist.printList(new_head)