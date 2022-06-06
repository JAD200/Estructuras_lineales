from module3_linked_lists.node import Node


class Stack():
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        """push Adds an element on top of the stack

        Args:
            data: Data to be added
        """
        node = Node(data)
        #   Puts the data at the top of the stack
        if self.top:
            node.next = self.top
            self.top = node
        else:  # Else makes the data the new node
            self.top = node

        self.size += 1

    def pop(self):
        """pop Removes an element at the top of the stack

        Returns:
            data: Data removed from the stack
        """
        #   If there is data on the stack removes the data at the top
        if self.top:
            data = self.top.data
            self.size -= 1
            #   In case there is more data on the stack
            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None

            return data

        else:
            return 'The stack is empty'

    def peek(self):
        """peek Shows the  data of the top of the stack

        Returns:
            data: Data at the top
        """
        if self.top:
            return self.top.data
        else:
            return 'The stack is empty'

    def clear(self):
        """clear Empties the stack
        """
        while self.top:
            self.pop()

# *  Challenges
    def search_element(self, data):
        node_returned = self.top
        if self.size > 0:
            while node_returned and node_returned.data != data:
                node_returned = node_returned.next

            if node_returned is None:
                print(f"Data '{data}' was not found!\n")
            else:
                print(f"Data '{data}' was found!\n")
        else:
            print('\nThe stack is empty\n')

    def iter(self):
        print('_' * 3, 'Stack data', '_' * 3)
        node_returned = self.top
        print('Size:', self.size, 'elements')
        while node_returned:
            current = node_returned.data
            node_returned = node_returned.next
            print('\t', current)

    def another_clear(self):
        self.top = None
        self.size = 0
        print('Stack emptied')

""" Code use in the shell to test the code
from stack import Stack
food = Stack()
food.push('egg')
food.push('ham')
food.push('spam')
food.pop()
#?  Expected:   'spam'
food.peek()
#?  Expected:   'ham'
food.clear()
food.peek()
#?  Expected:   'The stack is empty'
"""
if __name__ == '__main__':
    food = Stack()
    food.push('egg')
    food.push('ham')
    food.push('spam')

    food.search_element('ham')
    food.search_element('Nothing')

    food.iter()
    food.another_clear()
    food.search_element('egg')
    food.iter()
