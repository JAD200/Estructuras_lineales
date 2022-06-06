from module2_arrays.arrays import Array


class StackArray(Array):
    def __init__(self, capacity, fill_value=None):
        super().__init__(capacity, fill_value)
        self.capacity = capacity
        self.top = None
        self.size = 0

    def __str__(self):
        result = ''
        if self.size <= 0:
            return 'Stack empty'
        for i in self.items:
            if i != None:
                result += f'{i} '
        return result

    def push(self, data):
        if self.size == self.capacity:
            print('Stack full')
            return -1

        for i, value in enumerate(self.items):
            if value == None:
                self.items[i] = data
                self.top = data
                self.size += 1
                break

    def pop(self):
        for i in range(self.capacity-1, -1, -1):
            if self.items[i] != None:
                self.items[i] = None
                self.size -= 1
                print('Item removed: ', self.top)
                if i > 0:
                    self.top = self.items[i-1]
                else:
                    self.top = None
                break

    def peek(self):
        if self.top:
            print('\nItem a the top:', self.top)
        else:
            print("The stack is empty")

    def clear(self):
        self.__init__(self.capacity)
        print('Stack emptied')

    def search(self, target_item):
        if self.size <= 0:
            print("The stack is empty")
        else:
            if target_item in self.items:
                print(f"\nTarget item '{target_item}' was found")
                return self.items.index(target_item)
            else:
                print(f"\nTarget item '{target_item}' was not found")
                return -1

    def iter(self):
        for element in self.items:
            if element != None:
                yield element


if __name__ == '__main__':
    food = StackArray(3)
    food.push('egg')
    food.push('ham')
    food.push('spam')
    food.push('spm')
    food.pop()
    food.search('egg')
    food.search('Holi')
    food.peek()
    food.clear()
    food.peek()
