class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None

    def printlist(self):
        p = self.head
        while p is not None:
            print(p.data)
            p = p.next

genesis_node = SLinkedList()
genesis_node.head = Node('Mon')

node2 = Node('Tue')
node3 = Node('Wed')

# linking nodes
genesis_node.head.next = node2
node2.next = node3

genesis_node.printlist()