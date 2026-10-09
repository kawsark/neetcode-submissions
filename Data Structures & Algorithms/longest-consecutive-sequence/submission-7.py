class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsset = set(nums)
        print(numsset)
        cl = 1
        ml = 0
        # 2 3 4 5 10 20

        for n in numsset:
            if (n - 1) in numsset and (n-2) not in numsset:
                t = n
                cl = 0
                #print(f"Going to while loop with t = {t}")
                while (t - 1) in numsset:
                    t += 1
                    cl += 1
                #print(f"Broke out of while loop with cl = {cl}")

            ml = max(cl,ml)
            cl = 1

        return ml

        