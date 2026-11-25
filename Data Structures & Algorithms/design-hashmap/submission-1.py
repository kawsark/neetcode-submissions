# Meta: '{"felt":"Easy", "time": 25, "help": "none", "Comment": "Easier to use a list with list, instead of custom Linked List class. Note: tuples are immutable so use list of list"}'

class MyHashMap:

    def __init__(self):
        self.size = 997
        self.mymap = [None] * self.size
        

    def put(self, key: int, value: int) -> None:
        mk = key % self.size
        if self.mymap[mk] is None:
            self.mymap[mk] = []
        ml = self.mymap[mk]

        # Since tuples are immutable, remove and add
        for tup in ml:
            if tup[0] == key:
                tup[1] = value
                return None

        # New value
        ml.append([key,value])
        

    def get(self, key: int) -> int:
        tup = self.get_tuple(key)
        if tup:
            return tup[1]
        else:
            return -1        

    def remove(self, key: int) -> None:
        ml = self.get_list(key)
        for tup in ml:
            if tup[0] == key:
                ml.remove(tup)
                break
        
    def get_tuple(self, key):
        ml = self.get_list(key)
        for tup in ml:
            if tup[0] == key:
                return tup

        return None


    def get_list(self, key):
        mk = key % self.size
        if self.mymap[mk] is None:
            self.mymap[mk] = []
        
        return self.mymap[mk]

            



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)