class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # def push(self, data):
    #     node = LinkedListNode(data)
    #     node.next = self.head
    #     self.head = node

    # def insertAfter(self, prev, data):
    #     node = LinkedListNode(data)
    #     if prev is None:
    #         return
    #     node.next = prev.next
    #     prev.next = node

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

''' Iterative Approach '''

def reverseLinkedList(head):
    if head is None or head.next is None:
        return head
    prev = None
    while head is not None:
        temp = head.next
        head.next = prev
        prev = head
        head = temp
    return prev

if __name__ == '__main__':
    inp = list(map(int, input().split()))
    llist = LinkedList()
    for i in range(len(inp)):
        llist.append(inp[i])

    print("Linked List before reversal: ")
    llist.printList(llist.head)

    new_head = reverseLinkedList(llist.head)
    print("Linked List after reversal: ")
    llist.printList(new_head)