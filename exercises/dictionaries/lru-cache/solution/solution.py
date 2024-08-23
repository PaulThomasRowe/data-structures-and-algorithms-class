class LRUCache:
    def __init__(self, capacity, int):
        self.capacity = capacity
        self.cache = {}
        self.order = DoublyLinkedList()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.order.move_to_front(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.order.move_to_front(key)
        else:
            if len(self.cache) >= self.capacity:
                removed_key = self.order.remove_last()
                del self.cache[removed_key]
            self.cache[key] = value
            self.order.add_to_front(key)

class DoublyLinkedList:
    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.nodes = {}

    def add_to_front(self, key):
        node = ListNode(key)
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.nodes[key] = node

    def move_to_front(self, key):
        node = self.nodes[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        self.add_to_front(key)

    def remove_last(self):
        node = self.tail.prev
        node.prev.next = self.tail
        self.tail.prev = node.prev
        del self.nodes[node.key]
        return node.key

class ListNode:
    def __init__(self, key=None):
        self.key = key
        self.prev = None
        self.next = None
