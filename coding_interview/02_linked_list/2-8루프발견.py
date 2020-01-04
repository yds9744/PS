from linkedlist import Node
from linkedlist import LinkedList

def solution(linkedlist):
    dic = {}

    cur = linkedlist.head.next
    while cur:
        if cur in dic:
            print(cur.data)
            return cur
        else:
            dic[cur] = True
            cur = cur.next

    return False

ll = LinkedList(['A', 'B'])
c_node = Node('C')
ll.appendNode(c_node)
node = Node('D')
ll.appendNode(node)
node = Node('E')
node.next = c_node
ll.appendNode(node)

solution(ll)
