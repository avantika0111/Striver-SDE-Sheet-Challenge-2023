class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self, head):
        temp = head
        while temp:
            print(temp.data, end =" ")
            temp = temp.next
        print()

def getListAfterReverseOperation(head, n, b):
    
    if head is None:
        return head
    # create a dummy node that always points to the head
    dummy = Node(0)
    dummy.next = head

    # calculate the length of linked list
    temp = head
    l = 1
    while temp.next:
        l += 1
        temp = temp.next

    pre = dummy
    for i in range(n):
        k = b[i]
        if l < k:
            k = l
        if k == 0:
            continue
        cur = pre.next
        nex = cur.next
        for i in range(k-1):
            if nex is not None:
                cur.next = nex.next
                nex.next = pre.next
                pre.next = nex
                nex = cur.next
            
        l -= k
        pre = cur
        if l == 0:
            break

    return dummy.next

if __name__ == '__main__':
     #list1
    head = Node(1);
    head.next = Node(2);
    head.next.next = Node(3);
    head.next.next.next = Node(4);
    head.next.next.next.next = Node(5);
    head.next.next.next.next.next = Node(6);
    head.next.next.next.next.next.next = Node(7);
    n = 3
    k = [3, 3, 4]
    
    rev = LinkedList()
    revHead = getListAfterReverseOperation(head, n, k)
    rev.printList(revHead)