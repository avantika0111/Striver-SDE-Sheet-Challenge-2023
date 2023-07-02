class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def findIntersection(firstHead, secondHead):
	# # Method 1 by Hashing
    # hs = set()
    # p = firstHead
    # while p:
    #     hs.add(p)
    #     p = p.next
    
    # s = secondHead
    # while s:
    #     if s in hs:
    #         return s
    #     s = s.next

    # return None

    # # Method 2
    # l1 = 0
    # l2 = 0
    # a = firstHead
    # b = secondHead
    # while a != None or b != None:
    #     if a != None:
    #         l1 += 1
    #         a = a.next
    #     if b != None:
    #         l2 += 1
    #         b = b.next

    # a = firstHead
    # b = secondHead
    # if l1 > l2:
    #     diff = l1 - l2
    #     for i in range(diff):
    #         a = a.next
    # else:
    #     diff = l2 - l1
    #     for i in range(diff):
    #         b = b.next
    
    # while a is not None or b is not None:
    #     if a == b:
    #         return a
    #     a = a.next
    #     b = b.next
    # return None/

    # Method 3 (Recommended)
    a = firstHead
    b = secondHead
    while a != b:
        a = secondHead if a is None else a.next
        b = firstHead if b is None else b.next
        
    return a

if __name__ == '__main__':
    #list1
    head1 = Node(1);
    head1.next = Node(2);
    head1.next.next = Node(3);
    head1.next.next.next = Node(4);
    head1.next.next.next.next = Node(5);
    head1.next.next.next.next.next = Node(6);
    head1.next.next.next.next.next.next = Node(7);
    # list2
    head2 = Node(10);
    head2.next = Node(9);
    head2.next.next = Node(8);
    head2.next.next.next = head1.next.next.next;
    
    print("Intersection of two lists - ", findIntersection(head1, head2).data)
