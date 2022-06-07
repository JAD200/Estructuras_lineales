

class Queue:
    def __init__(self):
        self.inbound_stack = []
        self.outbound_stack = []

    def enqueue(self, data):
        self.inbound_stack.append(data)

    def dequeue(self):
        if not self.outbound_stack:
            while self.inbound_stack:
                self.outbound_stack.append(self.inbound_stack.pop())

        return self.outbound_stack.pop()


""" Code use in the shell to test the code
from stack_based_queue import Queue
numbers = Queue()
numbers.enqueue('5')
numbers.enqueue('6')
numbers.enqueue('7')
print(numbers.inbound_stack)
#?  Expected:   ['5', '6', '7']
numbers.dequeue()
#?  Expected:   '5'
print(numbers.inbound_stack)
#?  Expected:   []
print(numbers.outbound_stack)
#?  Expected:   ['6', '7']
"""
