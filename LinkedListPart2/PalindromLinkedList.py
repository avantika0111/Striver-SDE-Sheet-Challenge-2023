class Node:
    def __init__(self,data):
        
        self.data = data
        self.next = None
            
            
def middleElement(head):
    slow = head
    fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow

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

def isPalindrome(head):
    if head is None:
        return True
    # Step 1: Find Middle Element
    mid = middleElement(head)
    # Step 2: Reverse second half
    head2 = reverseLinkedList(mid)
    # Step 3: Compare first and second halves
    while head2 is not None:
        if head.data != head2.data:
            return False
        head= head.next
        head2 = head2.next

    return True

if __name__ == '__main__':
    head = Node(1);
    head.next = Node(2);
    head.next.next = Node(3);
    head.next.next.next = Node(4);
    head.next.next.next.next = Node(3);
    head.next.next.next.next.next = Node(2);
    head.next.next.next.next.next.next = Node(1);

    if isPalindrome(head):
        print("Palindrom")
    else:
        print("Not a palindrom")