from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        # head
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # initiate a ring
        if self.storage.length == 0:
            self.storage.add_to_head(item)
            self.current = self.storage.head

        # if NO capacity and current ISN'T at the HEAD -> remove from head -> add to tail
        elif self.storage.length == self.capacity and self.current is not self.storage.head:
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)

        #if NO capacity and current IS at the HEAD -> move current to tail
        elif self.storage.length == self.capacity:
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
            self.current = self.storage.tail

        #if IS capacity -> add to tail
        else:
            self.storage.add_to_tail(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        while len(list_buffer_contents) < self.storage.length:
            list_buffer_contents.append(self.current.value)
            if self.current.next:
                self.current = self.current.next
            else:
                self.current = self.storage.head
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
