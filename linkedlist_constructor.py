"""
Linked List implementation in Python.
Very simple and straightforward implementation of a LinkedList.
We have two constructors. One is LinkedList and another is Node.
Each node has a value and a pointer to the next node.
We make a linked list of three nodes 1 -> 3 -> 2 and
we print the linked list.
"""
class Node:
    def __init__(self, n):
        self.value = n
        self.next = None

class LinkedList:
    def __init__(self):
        self.head=None

    def printlinkedlist(self):
        current_node = self.head
        while(current_node):
            print(current_node.value)
            current_node = current_node.next
        
LL = LinkedList()
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

LL.head = n1
n1.next=n3
n3.next = n2

LL.printlinkedlist()
