class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class TwoWayNode(Node):
    def __init__(self, data, previous=None, next=None):
        Node.__init__(self, data, next)
        self.previous = previous


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, data):
        new_node = TwoWayNode(data, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.count += 1

    def dequeue(self):
        current = self.head

        if self.count == 1:
            self.count -= 1
            self.head == None
            self.tail == None
        elif self.count > 1:
            self.head = self.head.next
            self.head.previous = None
            self.count -= 1

        return current.data


""" Code use in the shell to test the code
from node_based_queue import Queue
food = Queue()
food.enqueue('eggs')
food.enqueue('ham')
food.enqueue('spam')
food.head.data
#?  Expected:   'eggs'
food.head.next.data
#?  Expected:   'ham'
food.tail.data
#?  Expected:   'spam'
food.tail.previous.data
#?  Expected:   'ham'
food.count
#?  Expected:   3
food.dequeue()
#?  Expected:   'eggs'
food.head.data
#?  Expected:   'ham'
"""
