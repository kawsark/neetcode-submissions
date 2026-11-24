# Meta: '{"felt":"medium", "time": 16, "help": "Solution", "Comment": "Using native list instead of a linked list"}'

class MyHashSet:

    def __init__(self):
        self.SIZE = 1000
        self.myset = [None] * self.SIZE
     
    def add(self, key: int) -> None:
        if not self.contains(key):
            self.get(key).append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.get(key).remove(key)

    def contains(self, key: int) -> bool:
        return key in self.get(key)
    
    def get(self, key) -> []:
        key_list = self.myset[key % self.SIZE]
        if not key_list:
            key_list = []
            self.myset[key % self.SIZE] = key_list
        return key_list



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)