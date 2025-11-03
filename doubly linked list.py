class Node(object):
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def prepend(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = self.tail = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def delete(self, val):
        curr = self.head
        while curr:
            if curr.val == val:
                if curr.prev:
                    curr.prev.next = curr.next
                else:
                    self.head = curr.next
                if curr.next:
                    curr.next.prev = curr.prev
                else:
                    self.tail = curr.prev
                return
            curr = curr.next

    def display_forward(self):
        res = []
        curr = self.head
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res

    def display_backward(self):
        res = []
        curr = self.tail
        while curr:
            res.append(curr.val)
            curr = curr.prev
        return res
