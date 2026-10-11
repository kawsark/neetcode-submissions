class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsset = set(nums)
        cl = 1
        ml = 0
        # 2 3 4 5 10 11 12 13 20 21
        visited = set()

        for n in numsset:
            t = n
            if (n - 1) in numsset and t not in visited:
                t = n
                cl = 0
                #print(f"Going to while loop with t = {t}")
                while (t - 1) in numsset:
                    visited.add(t)
                    t += 1
                    cl += 1
                #print(f"Broke out of while loop with cl = {cl}")

            ml = max(cl,ml)
            cl = 1

        return ml

        