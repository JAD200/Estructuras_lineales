from random import randint
from time import sleep
# TODO   Music player
#    Utilizar queues, añadir métodos para añadir canciones(enqueue) y reproducirlas(dequeue).
# !   Se reproducen en el orden añadido FIFO(FirstInFirstOut)


class MusicPlayer:
    def __init__(self):
        self.items = []
        self.size = 0

    def add_song(self, data):
        """add_song Adds a song in the list

        Args:
            data (str): Song to be added
        """
        self.items.insert(0, data)
        self.size += 1

    def reproduce(self):
        """reproduce Reproduces the first song added
        """
        data = self.items.pop()
        self.size -= 1
        print('Reproducing: ', data)

    def reproduce_all(self):
        """reproduce_all Reproduces all the songs in the list
        """
        while self.size > 0:
            song = self.items.pop()
            self.size -= 1
            print('Reproducing: ', song)
            sleep(randint(2, 3))  # *  Song length

    def show_list(self):
        """show_list Shows all the songs left in the list
        """
        total_items = self.size
        print('\n')
        if total_items == 0:
            print('-'*2, 'There are no songs in the list', '-'*2)
        else:
            print('_'*2, 'Showing songs in the list', '_'*2)
            for item in range(total_items):
                print(self.items[item])
        print('\n')


if __name__ == '__main__':
    list1 = MusicPlayer()
    list1.add_song('Imagine dragons - Radioactive')
    list1.add_song('Imagine dragons - Bones')
    list1.add_song('Imagine dragons - Enemy')
    list1.add_song('Imagine dragons - Next to you')
    list1.reproduce()
    list1.show_list()
    list1.reproduce_all()
    list1.show_list()
