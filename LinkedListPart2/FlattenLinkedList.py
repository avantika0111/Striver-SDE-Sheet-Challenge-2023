'''
Problem Statement: Given a Linked List of size N, where every node represents a sub-linked-list and contains two pointers:
(i) a next pointer to the next node,
(ii) a child pointer to a linked list where this node is head.
Each of the sub-linked-list is in sorted order.
Flatten the Link List such that all the nodes appear in a single level while maintaining the sorted order. 

Note: The flattened list will be printed using the child pointer instead of the next pointer.
'''
class Node:
    def __init__(self, val=0, next=None, child=None):
        self.data = val
        self.next = next
        self.child = child

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, head_ref, data):
        node = Node(data)
        node.child = head_ref
        head_ref = node
        return head_ref

    def printList(self, head):
        temp = head
        while temp:
            print(temp.data, end =" ")
            temp = temp.child
        print()

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
            first = first.child
        # link previous sorted node with next larger node in list2
        prev.child = second
        # swap
        temp = first
        first = second
        second = temp
    return res

def flattenLinkedList(head: Node) -> Node:
    if head is None or head.next is None:
        return head
    
    head.next = flattenLinkedList(head.next)
    # merge two list at a time and return the merged list
    head = sortTwoLists(head, head.next)
    return head

if __name__ == '__main__':
    L = LinkedList()
 
    '''
    Let us create the following linked list
            5 -> 10 -> 19 -> 28
            |    |     |     |
            V    V     V     V
            7    20    22    35
            |          |     |
            V          V     V
            8          50    40
            |                |
            V                V
            30               45
    '''
    L.head = L.push(L.head, 30)
    L.head = L.push(L.head, 8)
    L.head = L.push(L.head, 7)
    L.head = L.push(L.head, 5)
 
    L.head.next = L.push(L.head.next, 20)
    L.head.next = L.push(L.head.next, 10)
 
    L.head.next.next = L.push(L.head.next.next, 50)
    L.head.next.next = L.push(L.head.next.next, 22)
    L.head.next.next = L.push(L.head.next.next, 19)
 
    L.head.next.next.next = L.push(L.head.next.next.next, 45)
    L.head.next.next.next = L.push(L.head.next.next.next, 40)
    L.head.next.next.next = L.push(L.head.next.next.next, 35)
    L.head.next.next.next = L.push(L.head.next.next.next, 28)
 
    # Function call
    L.head = flattenLinkedList(L.head)
 
    L.printList(L.head)
