# Meta: '{"felt":"medium", "time": 25: , "help": "none", "Comment": "How to get O(1) time without a min heap?"}'
class MinStack:

    def __init__(self):
        self.st = []
        self.min_st = []

    def push(self, val: int) -> None:
        self.st.append(val)
        self.min_st.append(val)
        self.min_st.sort()

    def pop(self) -> None:
        v = self.st.pop()
        self.min_st.remove(v)
        
    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.min_st[0]
