# class from node.py
from node import Node


class SinglyLinkedList:
    """ Class to generate linked list made from nodes
    """

    def __init__(self):
        self.tail = None
        self.size = 0

    def append(self, data):
        """append add data to the linked list

        Args:
            data (str or int): data to be appended
        """
        node = Node(data)
    #   To make sure the tail is heading to a node
        if self.tail == None:
            self.tail = node
        else:
            current = self.tail

            while current.next:
                current = current.next

            current.next = node
    #   Add a node to the list size
        self.size += 1

    def size(self):
        return str(self.size)

    def iter(self):
        """iter Show all the data from the list

        Yields:
            str or int: saves the data while the code is running
        """
        current = self.tail

        while current:
            val = current.data
            current = current.next
            yield val

    def delete(self, data):
        """delete delete data from the list

        Args:
            data (str or int): data to be deleted

        Returns:
            str: data deleted
        """
        current = self.tail
        previous = self.tail

        while current:
            #   Data of current equals the data to delete
            if current.data == data:
                #   Makes the tail head to the next node
                if current == self.tail:
                    self.tail = current.next
                # * Makes previous equal the next node of current and returns the data deleted
                else:
                    previous.next = current.next
                    self.size -= 1
                    return current.data
            #   Now previous head to current and current to the next node
            previous = current
            current = current.next

    def search(self, data):
        for node in self.iter():
            if data == node:
                print(f'Data {data} found!')
            else:
                print(f"Data {data} wasn't found")

    def clear(self):
        """clear deleted all the node from the list
        """
        self.tail = None
        self.head = None
        self.size = 0


def show_list(list):
    print('* '*3, 'Lista', ' *'*3)
    for value in list.iter():
        print('\t', value)


if __name__ == '__main__':
## *  Code used to test the singly linked list
#     words = SinglyLinkedList()
# #   Try to add and delete specific data
#     words.append('spam')
#     words.append('eggs')
#     words.delete('eggs')
#     show_list(words)
# #   Search data
#     words.search('spam')
#     words.search('Holi')
# #   Clear the list
#     words.clear()
#     show_list(words)

# *  Challenge

    an_array = [1, 5, 6, 4]
    print(f'The array to convert\n{an_array}\n')
    data = SinglyLinkedList()

    for i in an_array:
        data.append(i)
        current = data.tail
    print('Linked list')
    while current:
        print(f'Node data: {current.data}')
        current = current.next
