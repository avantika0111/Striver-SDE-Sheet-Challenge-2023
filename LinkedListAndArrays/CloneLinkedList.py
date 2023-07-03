'''
Problem Statement: Given a Linked list that has two pointers in each node 
and one of which points to the first node and the other points to any random node. 
Write a program to clone the LinkedList
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.random = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self, head):
        result = []
        while head:
            result.append(f"{head.data}({head.random.data})")
            head = head.next
        print(" -> ".join(result))

'''
Approach 1 - Using Hashing
TC - O(N) + O(N) 
SC - O(N)
'''
def cloneRandomList1(head):
    if head is None:
        return None
        
    hm = dict()
    temp = head
    while temp is not None:
        hm[temp] = Node(temp.data)
        temp = temp.next

    temp = head
    while temp:
        node = hm[temp]
        node.next = temp.next if temp.next is not None else None
        node.random = temp.random if temp.random is not None else None
        temp = temp.next
    
    return hm[head]

'''
Optimal Solution
TC - O(N) + O(N) + O(N)
SC - O(1)
'''
def cloneRandomList2(head):
    if head is None:
        return None

    # Step 1 - Create copy nodes and put them in between original ones
    temp = head
    while temp:
        node = Node(temp.data)
        node.next = temp.next
        temp.next = node
        temp = temp.next.next
    
    # step 2 - point random pointers of copy nodes to correct positions
    temp2 = head
    while temp2:
        if temp2.random is not None:
            temp2.next.random = temp2.random.next
        temp2 = temp2.next.next
    
    # step3 - separate original from deep copy
    dummy = Node(0)
    p = dummy
    i = head
    while i:
        front = i.next.next
        p.next = i.next
        i.next = front
        p = p.next
        i = front

    return dummy.next

if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.random = head.next.next
    head.next.random = head
    head.next.next.random = head.next.next.next.next
    head.next.next.next.random = head.next.next
    head.next.next.next.next.random = head.next
    L = LinkedList()
    # Print the original list
    print("The original linked list:")
    L.printList(head)
    
    # Function call
    # sol = cloneRandomList(head)
    sol = cloneRandomList2(head)
    
    print("The cloned linked list:")
    L.printList(sol)
