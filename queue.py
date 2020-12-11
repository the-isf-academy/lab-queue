# queue.py
# by Jacob Wolf
#
# Queue implementation to be used in the online shopping sevice test

class QueueItem:
    """ List item for a singlely linked list containing data and optional next property.
    """

    def __init__(self, data, next_obj=None):
        self.data = data
        self.next = next_obj


class Queue:
    """ Queue interface implemented with a singlely linked list.
    """

    def __init__(self):
        self.head = None

    def __getitem__(self, key):
        curr = self.head
        for i in range(key):
            try:
                curr = curr.next
            except:
                raise IndexError
        try:
            return curr.data
        except:
            raise IndexError

    def enqueue(self, data):
        """Enqueues data into the list.
        """
        item = QueueItem(data)
        if self.head:
            curr = self.head
            nxt = self.head.next
            while nxt:
                curr = nxt
                nxt = curr.next
            curr.next = item
        else:
            self.head = item

    def dequeue(self):
        """Dequeues the first thing in the list.
        """
        item = None
        if self.head:
            item = self.head.data
            self.head = self.head.next
        return item

    def length(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count
