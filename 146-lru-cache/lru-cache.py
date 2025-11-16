class Node :
    def __init__(self,key,value) :
        self.key = key
        self.value = value
        self.next = self.prev = None

class LRUCache:
    hsmap = dict()
    capacity = count = 0
    head = tail = None

    def __init__(self, capacity: int):
        self.hsmap = dict()
        self.capacity = capacity
        self.head = Node(0,0) 
        self.tail = Node(0,0)

        self.head.next = self.tail
        self.head.prev = None
        self.tail.next = None
        self.tail.prev = self.head
        count = 0

    def add(self , node) :
        node.next = self.head.next
        node.next.prev = node
        node.prev = self.head
        self.head.next = node

    def delete(self, node) :
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key in self.hsmap :
            node = self.hsmap[key]
            result = node.value
            self.delete(node)
            self.add(node)
            return result
        else :
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hsmap :
            node = self.hsmap[key]
            node.value = value
            self.delete(node)
            self.add(node)
        else :
            node = Node(key,value)
            self.hsmap[key] = node

            if self.count < self.capacity :
                self.count += 1
                self.add(node)
            else :
                self.hsmap.pop(self.tail.prev.key)
                self.delete(self.tail.prev)
                self.add(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)