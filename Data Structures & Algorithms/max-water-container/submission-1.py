class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        res = 0

        while left < right:
            hr = heights[right]
            hl = heights[left]
            area = (right - left) * min(hl,hr)
            res = max(res,area)

            if hl < hr:
                left += 1
            else:
                right -= 1


        return res