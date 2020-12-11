# queue.py
# by Jacob Wolf
#
# Queue implementation to be used in the online shopping sevice test

class SinglelyLinkedListItem:
    """ List item for a singlely linked list containing data and optional next property.
    """

    def __init__(self, data, next_obj=None):
        self.data = data
        self.next = next_obj


class SinglelyLinkedList:
    """ Queue interface implemented with a singlely linked list.
    """

    def __init__(self):
        self.head = None

    def enqueue(self, data):
        """Enqueues data into the list.
        """
        item = SinglelyLinkedListItem(data)
        if self.head:
            curr = self.head
            nxt = self.head.next
            while nxt:
                curr = nxt
                nxt = curr.next
            curr.next = item
        else:
            self.head = item

    def length(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count
