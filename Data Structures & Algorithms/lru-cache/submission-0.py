class Node:
    def __init__(self):
        self.key = -1
        self.value = -1
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.max_capacity = capacity
        self.cur_capacity = 0
        self.key_to_node = {}
        self.LRU = None
        self.MRU = None
    
    def reassignToMRU(self, p):
        p.prev = None
        p.next = self.MRU
        self.MRU.prev = p
        self.MRU = p

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1

        p = self.key_to_node[key]

        if self.cur_capacity > 1:
            if p.key == self.LRU.key:
                self.LRU = self.LRU.prev
                self.LRU.next = None
                self.reassignToMRU(p)
            elif p.key != self.MRU.key:
                p.prev.next = p.next
                p.next.prev = p.prev
                self.reassignToMRU(p)
        
        return self.MRU.value
        
        # Get the pointer to the node from the hash map
        # We can now retrieve the value, but before doing that we need to move it to the tail

        # This can be a separate function moveToTail()
        # If this is head, give head to next in line
        # Rewire its prev and next pointers
            # The nodes that point to it should point at each other
            # This node should go to the end and become the new tail
        # Rewire the current tail to point to it
            # Then reassign the new tail

    def put(self, key: int, value: int) -> None:
        if self.cur_capacity == 0:
            self.key_to_node[key] = Node()
            p = self.key_to_node[key]
            p.key, p.value = key, value
            self.LRU, self.MRU = p, p
            self.cur_capacity += 1
        elif key in self.key_to_node:
            self.get(key)
            p = self.key_to_node[key]
            p.value = value
        elif self.cur_capacity < self.max_capacity:
            self.key_to_node[key] = Node()
            p = self.key_to_node[key]
            p.key, p.value = key, value
            self.reassignToMRU(p)
            self.cur_capacity += 1
        else:
            self.key_to_node[key] = Node()
            p = self.key_to_node[key]
            p.key, p.value = key, value

            if self.cur_capacity == 1:
                temp = self.LRU
                self.LRU = p
            else:
                temp = self.LRU
                self.LRU = self.LRU.prev
                self.LRU.next = None
                temp.prev = None

            del self.key_to_node[temp.key]

            self.reassignToMRU(p)

        # 3 cases
        # 1. We are putting a new key-val but the cache is not full yet
            # We know this by checking current capacity
            # Give it a node and a pointer in the hash map
            # Put it at the tail
            # Update the current capacity
        # 2. We are updating a current key-val with a new val
            # We know this by checking that the key is already in the hash map
            # Update the value with the new value at the node
            # Then moveToTail()
        # 3. We are putting a new key-val and the cache is already full --> need to evict LRU
            # Move head to next in line
            # Detach its pointers
            # Remove its entry from hash map
            # Give the new key-val a node and a pointer in the hash map
            # Put it at the tail
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)