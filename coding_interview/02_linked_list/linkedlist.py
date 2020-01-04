# define Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# define Linked_List class
class LinkedList:
    def __init__(self, data_lst=[]):
        self.head = Node("dummy")
        cur = self.head
        for i in data_lst:
            cur.next = Node(i)
            cur = cur.next
        self.tail = cur
        self.len = len(data_lst)

    def append(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node
        self.len += 1
        
    def appendNode(self, node):
        self.tail.next = node
        self.tail = node
        self.len += 1

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head.next
        self.head.next = new_node

    def print(self):
        cur = self.head
        while cur.next:
            cur = cur.next
            print(cur.data, end=" ")
        print()
