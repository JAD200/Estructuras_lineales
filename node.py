"""
Code used for the class 'Nodos y singly linked list'.

All the code but the 'Node' class is written in the shell
for demonstrative purposes.

The node methods should be incorporated into the Node class.
"""


class Node():
    #*  Represents a single linked node.

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# Creating 3 different nodes
node1 = None
node2 = Node("A", None)
node3 = Node("B", node2)

# This causes an Attribute Error
# node1.next = node3

node1 = Node("C", node3)
