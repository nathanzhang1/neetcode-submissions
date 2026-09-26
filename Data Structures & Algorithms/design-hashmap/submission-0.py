class Node:
    def __init__(self):
        self.key = -1
        self.val = -1
        self.next = None

class MyHashMap:

    def __init__(self):
        self.map = [Node() for _ in range(1000)]

    def put(self, key: int, value: int) -> None:
        index = key % len(self.map)
        p = self.map[index]
        while p.next:
            p = p.next
            if p.key == key:
                p.val = value
                return
        p.next = Node()
        p.next.key, p.next.val = key, value

    def get(self, key: int) -> int:
        index = key % len(self.map)
        p = self.map[index]
        while p.next and p.key != key:
            p = p.next
        return p.val if p.key == key else -1

    def remove(self, key: int) -> None:
        index = key % len(self.map)
        p = self.map[index]
        while p.next and p.next.key != key:
            p = p.next
        if not p.next:
            return
        temp = p.next.next
        p.next.next = None
        p.next = temp