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

    def __len__(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count

    def append(self, data):
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

    def popleft(self):
        """Dequeues the first thing in the list.
        """
        if self.head:
            item = self.head.data
            self.head = self.head.next
            return item
        else:
            raise IndexError

    def insert(self, index, data):
        """Inserts an element into the queue at a particular
        index.
        """
        item = QueueItem(data)
        prev = None
        curr = self.head
        count = 0
        while curr:
            if count == index:
                break
            prev = curr
            curr = curr.next
            count += 1
        if prev:
            prev.next = item
        else:
            self.head = item
        item.next = curr
        
    def remove(self, value):
        """Removes the first instance of a value from the queue.
        Throuws an error if the value doesn't exist in the list.
        """
        prev = None
        curr = self.head
        while(curr):
            if value == curr.data:
                if prev:
                    prev.next = curr.next
                    return
                else:
                    self.head = curr.next
                    return
            prev = curr
            curr = curr.next
        raise ValueError

    def index(self, value):
        """Finds the first instance of a value within the queue and
        returns the index of the value.
        """
        curr = self.head
        count = 0
        while(curr):
            if value == curr.data:
                return count
            curr = curr.next
            count += 1
        raise ValueError

    def count(self, value):
        """Counts the number of times a value appears in the queue
        and returns the count.
        """
        curr = self.head
        count = 0
        while curr:
            if curr.data == value:
                count += 1
            curr = curr.next
        return count
