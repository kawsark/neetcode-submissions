# Meta: '{"felt":"easy", "time": 10, "help": "none", "Comment": "Binary search, remember the 3 rules"}'

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        mid = 0

        while left <= right:
            mid = left + (right-left) // 2
            #print(f"{left} | {mid} | {right}")
            res = guess(mid)
            if res == 0:
                return mid
            elif res == -1:
                right = mid - 1
            else: #res == +1
                left = mid + 1
        
        return mid