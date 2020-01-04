from linkedlist import Node 
from linkedlist import LinkedList

# solution : with hash buffer
def solution(linkedlist):
    dic = {}
    cur = linkedlist.head
    
    while cur.next:
        if cur.next.data in dic:
            cur.next = cur.next.next
        else:
            dic[cur.next.data] = True
            cur = cur.next

    linkedlist.print()
    return linkedlist

# solution : w/o buffer
def solution_wo_buffer(linkedlist):
    cur = linkedlist.head
    cur = cur.next
    
    while cur:
        run = cur
        while run.next:
            if run.next.data == cur.data:
                run.next = run.next.next
            else:
                run = run.next
        cur = cur.next
                
    linkedlist.print()
    return linkedlist



# test
solution(LinkedList([1, 2, 3, 4, 1, 2, 6, 1, 2]))
solution_wo_buffer(LinkedList([1, 2, 3, 4, 1, 2, 6, 1, 2]))
