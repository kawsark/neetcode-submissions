# Meta: '{"felt":"medium", "time": 25, "help": "Solution", "Comment": "the previous left case is tricky. Binary search itself was easy"}'
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        left = 1
        right = x
        mid = prev_left_mid = 0

        while left <= right:
            mid = left + (right - left) // 2
            res = mid * mid
            if res == x:
                return mid
            elif res < x:
                prev_left_mid = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return prev_left_mid
