class Solution:

    def __init__(self):
        self.stepsmap = { 1: 1, 2: 2}


    def steps(self, n: int):
        if n in self.stepsmap:
            return self.stepsmap[n]
        
        # Need to calculate recursively
        res = self.steps(n-1) + self.steps(n-2)
        self.stepsmap[n] = res

        return res

    def climbStairs(self, n: int) -> int:
               
        return self.steps(n)