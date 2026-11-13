# Meta: '{"felt":"medium", "time": 20, "help":"video solution", "Comment": "Wow ended up being pretty easy after watching the solution, just needed to store tuples"}'
class MinStack:

    def __init__(self):
        self.st = []
        self.minimum = float('Inf')

    def push(self, val: int) -> None:
        self.minimum = min(self.minimum, val)
        self.st.append((val,self.minimum))

    def pop(self) -> None:
        self.st.pop()
        if len(self.st) > 0:
            self.minimum = self.getMin()
        else:
            self.minimum = float('Inf')

    def top(self) -> int:
        return self.st[-1][0]

    def getMin(self) -> int:
        return self.st[-1][1]
        
