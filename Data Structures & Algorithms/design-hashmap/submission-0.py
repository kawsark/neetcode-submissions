class Element:
    
    next: Element

    def __init__(self, k: int, v: int = None):
        self.key = k
        self.val = v
        self.next = None

class MyHashMap:

    size = 1000
    maplist: [Element]

    def __init__(self):
        self.maplist = [None] * self.size
        for i in range(self.size):
            self.maplist[i] = Element(-1)

    def put(self, key: int, value: int) -> None:
        slot = key % self.size

        e = self.maplist[slot]
        while e.next:
            e = e.next
            if e.key == key: # Found element, update the value
                e.val = value
                return

        # The element did not exist
        ne = Element(key,value)
        if not e:
            e = self.maplist[slot]
        e.next = ne

    def get(self, key: int) -> int:
        slot = key % self.size
        e = self.maplist[slot]
        while e.next:
            e = e.next
            if e.key == key:
                return e.val

        return -1 

    def remove(self, key: int) -> None:
        slot = key % self.size
        e = self.maplist[slot]
        p = None

        while e.next:
            p = e
            e = e.next
            if e.key == key: # Found element
                p.next = e.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)