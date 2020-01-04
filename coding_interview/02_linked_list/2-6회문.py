from linkedlist import Node
from linkedlist import LinkedList

def solution(linkedlist):
    # make reverse linked_list
    reverse = LinkedList()
    cur = linkedlist.head
    while cur.next:
        cur = cur.next
        reverse.prepend(cur.data)

    linkedlist.print()
    reverse.print()

    # compare linked_list with reversed one
    cur = linkedlist.head
    recur = reverse.head
    while cur.next and recur.next:
        cur = cur.next
        recur = recur.next
        if cur.data != recur.data:
            return False
    return True


# test
print(solution(LinkedList([1, 2, 4, 3, 2, 1])))
