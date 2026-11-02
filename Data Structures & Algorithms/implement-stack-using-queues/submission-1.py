# Meta: '{"felt":"easy", "time": 13, "help": "none"}'
class MyStack:

    def __init__(self):
        self._queues = [[], []]
        self._green = 0
        self._blue = 1

    def push(self, x: int) -> None:
        green = self._queues[self._green]
        blue = self._queues[self._blue]

        green.insert(0, x)
        while len(blue) > 0:
            green.insert(0, blue.pop())
        
        self._green = not self._green
        self._blue = not self._blue

    def pop(self) -> int:
        return self._queues[self._blue].pop()
        

    def top(self) -> int:
        return self._queues[self._blue][-1]
        

    def empty(self) -> bool:
        return len(self._queues[self._blue]) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()