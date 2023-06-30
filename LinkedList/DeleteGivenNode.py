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

def deleteNode(head, node):
    node.data = node.next.data
    node.next = node.next.next
    return head

if __name__ == '__main__':
    inp = list(map(int, input("Enter Linked List Elements - ").split()))
    k = int(input("Enter node to delete - "))
    llist = LinkedList()
    for i in range(len(inp)):
        llist.append(inp[i])
    node = llist.head
    for i in range(1, k):
        node = node.next
    new_head = deleteNode(llist.head, node)
    print("Linked List after deleting node: ")
    llist.printList(new_head)