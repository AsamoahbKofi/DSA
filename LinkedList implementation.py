class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_at_beginning(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("Done")

    def insert_at_end(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node

    def insert_at_any_position(self, data, position):
        node = Node(data)
        current = self.head
        if position == 1:
            node.next = self.head
            self.head = node
            return
        for _ in range(position - 2):
            if current is None:
                print("Out of Range")
                return
            current = current.next
        if current is None:
            print("Out of Range")
            return
        node.next = current.next
        current.next = node

    def deletion(self, key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            current = None
            return
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if current is None:
            print("Outta Bounds")
            return
        prev.next = current.next
        current = None

    def get_length(self):
        current = self.head
        count = 0
        while current:
            current = current.next
            count += 1
        return f'Length = {count}'

    def deletion_using_index(self, position):
        current = self.head
        if position == 1:
            self.head = current.next
            current = None
            return
        prev = None
        for _ in range(position - 1):
            if current is None:
                print("Out of Range")
                return
            prev = current
            current = current.next
        if current is None:
            print("Out of Range")
            return
        prev.next = current.next
        current = None

    def search_node(self, data):
        current = self.head
        count = 0
        while current:
            if current.data == data:
                print(f'{data} is found at index {count}')
                return
            current = current.next
            count += 1
        print("Outta bound")

    def update_node(self, old_node, new_node):
        current = self.head
        if current and current.data == old_node:
            current.data = new_node
            return
        while current and current.data != old_node:
            current = current.next
        if current is None:
            print("Outta Bounds")
            return
        current.data = new_node

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

llist = LinkedList()
llist.insert_at_beginning(24)
llist.insert_at_beginning(23)
llist.insert_at_beginning(22)
llist.insert_at_beginning(30)
llist.insert_at_end(300)
llist.insert_at_any_position(23.5, 3)
llist.deletion(23.5)
print(llist.get_length())
llist.deletion_using_index(3)
llist.search_node(300)
llist.update_node(24, 25)
print("\nOriginal Linked List")
llist.traverse()

llist.reverse()
print("\nReversed Linked List")
llist.traverse()
