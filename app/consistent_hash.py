import bisect
import hashlib

class ConsistentHash:
    def __init__(self, num_slots=512, num_replicas=9):
        self.num_slots = num_slots
        self.num_replicas = num_replicas
        self.slots = []
        self.nodes = {}

    def _hash(self, key):
        return int(hashlib.md5(key.encode('utf-8')).hexdigest(), 16) % self.num_slots

    def add_node(self, node):
        for i in range(self.num_replicas):
            virtual_node = f"{node}-{i}"
            hashed_key = self._hash(virtual_node)
            bisect.insort(self.slots, hashed_key)
            self.nodes[hashed_key] = node

    def remove_node(self, node):
        for i in range(self.num_replicas):
            virtual_node = f"{node}-{i}"
            hashed_key = self._hash(virtual_node)
            self.slots.remove(hashed_key)
            del self.nodes[hashed_key]

    def get_node(self, key):
        hashed_key = self._hash(key)
        index = bisect.bisect(self.slots, hashed_key) % len(self.slots)
        return self.nodes[self.slots[index]]
