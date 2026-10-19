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
        # Memoization approach
        # return self.steps(n)

        # Tabulation approach
        nm = [1 , 2]
        if n < 3:
            return nm[n-1]

        for i in range(3, n+1):
            c = nm[0] + nm[1]
            nm[0] = nm[1]
            nm[1] = c

        return nm[1]
        