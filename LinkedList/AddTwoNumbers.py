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



def addTwoNumbers(head1, head2):
    # Write your code here.
    res = LinkedListNode(0)
    temp = res
    carry = 0
    while (head1 or head2) or carry:
        s = 0
        if head1 is not None:
            s += head1.data
            head1 = head1.next
        if head2 is not None:
            s += head2.data
            head2 = head2.next
        s += carry
        carry = s // 10
        node = LinkedListNode(s % 10)
        temp.next = node
        temp = temp.next
    return res.next

if __name__ == '__main__':
    list1 = list(map(int, input("Enter the first linked list elements - ").split()))
    list2 = list(map(int, input("Enter the second linked list elements - ").split()))
    l1 = LinkedList()
    l2 = LinkedList()
    for i in range(len(list1)):
        l1.append(list1[i])
    for i in range(len(list2)):
        l2.append(list2[i])
    
    new_head = addTwoNumbers(l1.head, l2.head)
    print("Sum of two lists - ")
    l1.printList(new_head)