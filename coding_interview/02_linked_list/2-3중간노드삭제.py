from linkedlist import Node 
from linkedlist import LinkedList

def solution(linkedlist, node):
    if node.next:
        node.data = node.next.data
        node.next = node.next.next
        linkedlist.print()
        return linkedlist
    else:
        return False

# test
ll = LinkedList([3, 2, 1])
node = Node(44)
ll.appendNode(node)
ll.append(1)
ll.append(2)
ll.append(3)
ll.print()
solution(ll, node)
