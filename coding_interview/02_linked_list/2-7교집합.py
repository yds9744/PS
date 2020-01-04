from linkedlist import Node
from linkedlist import LinkedList

def solution(lst1, lst2):
    answer = []
    
    # put node of list to stack
    stk1 = []
    stk2 = []
    cur1 = lst1.head.next
    cur2 = lst2.head.next
    while cur1:
        stk1.append(cur1)
        cur1 = cur1.next
    while cur2:
        stk2.append(cur2)
        cur2 = cur2.next

    # find!
    while stk1 and stk2:
        p1 = stk1.pop()
        p2 = stk2.pop()
        if p1 == p2:
            answer.append(p1)
            print(p1.data)
        else: break

    return answer


lst1 = LinkedList([3])
lst2 = LinkedList([2, 4, 3])

for i in range(5):
    node = Node(i)
    lst1.appendNode(node)
    lst2.appendNode(node)

node = solution(lst1, lst2)
