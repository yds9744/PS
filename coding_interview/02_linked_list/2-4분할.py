from linkedlist import Node
from linkedlist import LinkedList

def solution(ll, x):
    cur = ll.head

    # O(n)
    for i in range(ll.len):
        if cur.next.data >= x:
            # add on tmp and delete
            tmp = cur.next
            cur.next = cur.next.next
            # add tmp to the tail
            ll.tail.next = tmp
            ll.tail = tmp
            ll.tail.next = None
        else:
            cur = cur.next

    ll.print()

solution(LinkedList([3, 5, 8, 5, 10, 2, 1]), 5)
    
