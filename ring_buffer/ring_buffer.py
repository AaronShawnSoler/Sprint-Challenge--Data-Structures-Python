from doubly_linked_list import DoublyLinkedList
from queue import Queue
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        self.storage.add_to_head(item)
        size = self.storage.__len__()
        # print(size)
        if size > self.capacity:
            self.storage.remove_from_tail()


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here


        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
