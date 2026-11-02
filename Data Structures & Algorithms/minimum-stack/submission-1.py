# Meta: '{"felt":"medium", "time": 20, "help":"claude"}'
class MinStack:

    def __init__(self):
        self.st = []
        self.min_st = []

    def push(self, val: int) -> None:
        self.st.append(val)
        if len(self.min_st) == 0 or val <= self.min_st[-1]:
            self.min_st.append(val)

    def pop(self) -> None:
        val = self.st.pop()
        if len(self.min_st) > 0 and val == self.min_st[-1]:
            self.min_st.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.min_st[-1]
        
