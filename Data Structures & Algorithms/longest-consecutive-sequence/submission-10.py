class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsset = set(nums)
        cl = 1
        ml = 0
        # 2 3 4 5 10 11 12 13 20 21

        for n in numsset:
            if (n - 1) not in numsset:
                cl = 1
                #print(f"Going to while loop with t = {t}")
                while (n + cl) in numsset:
                    cl += 1
                #print(f"Broke out of while loop with cl = {cl}")

            ml = max(cl,ml)
            cl = 1

        return ml

        