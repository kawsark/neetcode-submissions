class Solution:
    def tribonacci(self, n: int) -> int:

        # Simplfying: Tn = Tn-3 + Tn-2 + Tn-1
        tri = [0, 1, 1 ]
        
        if n <= 2:
            return tri[n]

        i = 3
        while i <= n:
            current = sum(tri)
            tri[0] = tri[1]
            tri[1] = tri[2]
            tri[2] = current
            i += 1
        
        return tri[2]


        