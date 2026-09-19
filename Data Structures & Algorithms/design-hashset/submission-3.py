class Element:

    _x: object
    _n: Element

    def __init__(self, x: object):
        self._x = x
        self._n = None

    def setnext(self, n: Element):
        if self._n and n:
            n.setnext(self._n)

        self._n = n

class MyHashSet:

    mylist: list
    size = int(1000)
    elements = 0

    def __init__(self):
        self.mylist = [None] * self.size

    def add(self, key: int) -> None:
        if not self.contains(key):
            slot = key % self.size # [10] 1 -> 2 -> 3
            e = Element(key)
            if not self.mylist[slot]:
                self.mylist[slot] = e
            else:
                self.mylist[slot].setnext(e)
            self.elements += 1
            

    def remove(self, key: int) -> None:
        slot = key % self.size
        e = self.mylist[slot] # [10] 1 -> 2 -> 3
        p = None
        while e:
            if e._x == key:
                if not p: # First element
                    if e._n:
                        self.mylist[slot] = e._n
                    else:
                        self.mylist[slot] = None
                else: # Linked element
                    p._n = e._n
                    
                e = None
                self.elements -= 1

            else:
                p = e
                e = e._n

    def contains(self, key: int) -> bool:
        slot = key % self.size
        e = self.mylist[slot]
        while e:
            if e._x == key:
                return True
            else:
                e = e._n
        
        return False


        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)