from double_linked_list import TwoWayNode

#   Circle Double Linked List
class circleDoubleLinkedList():
    def __init__(self):
        self.head = TwoWayNode(None, None, None)
        self.tail = self.head
        self.size = 0

        self.head.next = self.tail
        self.head.previous = self.tail

    def range(self, start, stop):
        # * Creación de los nodos enlazados (linked list)
        self.head = TwoWayNode(start, next=None, previous=None)
        self.tail = self.head
        self.size = 1

        for data in range(start+1, stop):
            self.tail.next = TwoWayNode(data, previous=self.tail)
            self.tail = self.tail.next
            self.size += 1

        self.tail.next = self.head
        self.head.previous = self.tail

    def __str__(self):
        # * Recorrer e imprimir valores de la lista
        probe = self.head
        result = ''
        while probe.next != self.head:
            result += f'{probe.data} '
            probe = probe.next
        result += f'{probe.data}'
        result = result.strip()
        return result

    def reverse(self):
        probe = self.tail
        result = ''
        while probe.previous != self.tail:
            result += f'{probe.data} '
            probe = probe.previous
        result += f'{probe.data}'
        result = result.strip()
        return result

    def str_by_steps(self, steps, direction='forward'):
        result = ''

        if direction == 'forward':
            probe = self.head
            while steps > 0:
                result += f'{probe.data} '
                probe = probe.next
                steps -= 1

        if direction == 'backward':
            probe = self.tail
            while steps > 0:
                result += f'{probe.data} '
                probe = probe.previous
                steps -= 1

        result = result.strip()
        return result

    def search(self, target_item):
        # * Búsqueda de un elemento
        probe = self.head
        while probe.next != self.head and target_item != probe.data:
            probe = probe.next

        if probe.data == target_item:
            print(f'Target item {target_item} has been found')
            return probe
        else:
            print(f'Target item {target_item} is not in the linked list')
            return -1

    def replace(self, target_item, new_item):
        # * Remplazo de un elemento
        probe = self.head

        while probe.next != self.head and target_item != probe.data:
            probe = probe.next

        if probe.data == target_item:
            probe.data = new_item
            print(
                f"{new_item} replace the old value {target_item}")
        else:
            print(f"The target item {target_item} is not in the linked list")

    def unchanged(self, new_item):
        # * Insertar un nuevo elemento/nodo al inicio(head)
        if self.size == 0:
            self.head.data = new_item
        else:
            self.head = TwoWayNode(
                new_item, previous=self.tail, next=self.head)
            self.head.next.previous = self.head
            self.tail.next = self.head
        self.size += 1

    def append(self, new_item):
        # * Insertar un nuevo elemento/nodo al final(tail)
        if self.size == 0:
            self.tail.data = new_item
        else:
            self.tail = TwoWayNode(
                new_item, previous=self.tail, next=self.head)
            self.tail.previous.next = self.tail
            self.head.previous = self.tail
        self.size += 1

    def changed(self):
        # * Eliminar un elemento/nodo al inicio(head)
        if self.size == 0:
            return None

        removed_item = self.head.data
        self.head = self.head.next

        self.head.previous = self.tail
        self.tail.next = self.head

        self.size -= 1

        print(f'Removed_item: {removed_item}')
        return removed_item

    def pop(self):
        # * Eliminar un elemento/nodo al final(tail)
        if self.size == 0:
            return None

        removed_item = self.tail.data
        self.tail = self.tail.previous

        self.head.previous = self.tail
        self.tail.next = self.head

        self.size -= 1

        print(f'Removed_item: {removed_item}')
        return removed_item

    def insert(self, new_item, index):
        # * Agregar un nuevo elemento/nodo por "indice" (Cuenta de Head - Tail)
        if self.size == 0:
            self.head.data = new_item
            self.size += 1
        elif index <= 0:
            self.unchanged(new_item)
        elif index >= self.size - 1:
            self.append(new_item)
        else:
            probe = self.head
            while index > 1 and probe.next != self.head:
                probe = probe.next
                index -= 1
            probe.next = TwoWayNode(new_item, previous=probe, next=probe.next)
            probe.next.next.previous = probe.next
            self.size += 1

    def delete_by_index(self, index):
        # * Eliminar un nuevo elemento/nodo por "indice" (Cuenta de Head - Tail)
        if self.size == 0:
            return None
        if index <= 0:
            self.changed()
        elif index >= self.size - 1:
            self.pop()
        else:
            probe = self.head
            while index > 1 and probe.next.next != self.head:
                probe = probe.next
                index -= 1
            removed_item = probe.next.data
            probe.next = probe.next.next
            probe.next.previous = probe
            self.size -= 1

            print(f'Removed_item: {removed_item}')
            return removed_item

    def clear(self):
        self.__init__()
