from linkedlist import Node 
from linkedlist import LinkedList

def solution(linkedlist, k):
    # cur: 1, run: k (k-1 differs)
    cur = linkedlist.head.next
    run = cur
    for i in range(k-1):
        run = run.next

    # cur: n-k+1, run: n (k-1 differs)
    while run.next:
        cur = cur.next
        run = run.next

    return cur.data

# test
print(solution(LinkedList([1, 2, 3, 4, 1, 2, 6, 1, 2]), 3))
