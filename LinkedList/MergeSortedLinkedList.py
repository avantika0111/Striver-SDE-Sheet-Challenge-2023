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

# In-place sort

def sortTwoLists(first, second):
    if first is None:
        return second
    if second is None:
        return first

    # swap first and second as we want first to always point to smaller value
    if second.data < first.data:
        temp = first
        first = second
        second = temp
    
    # this will be the new head of the final linked list
    res = first

    while first is not None and second is not None:
        # prev will store the last sorted node
        prev = None

        while first is not None and first.data <= second. data:
            prev = first
            first = first.next

        # link previous sorted node with next larger node in list2
        prev.next = second

        # swap
        temp = first
        first = second
        second = temp
    
    return res

if __name__ == '__main__':
    list1 = list(map(int, input("Enter the first linked list elements - ").split()))
    list2 = list(map(int, input("Enter the second linked list elements - ").split()))
    l1 = LinkedList()
    l2 = LinkedList()
    for i in range(len(list1)):
        l1.append(list1[i])
    for i in range(len(list2)):
        l2.append(list2[i])
    
    new_head = sortTwoLists(l1.head, l2.head)
    l1.printList(new_head)