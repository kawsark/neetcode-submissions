class Solution:

    def isValid(self, right: int, left: int, charsmap, k) -> bool:
        most_freq = 0
        # Obtain most frequent
        for c in charsmap:
            most_freq = max(most_freq, charsmap.get(c))

        return (right - left) + 1 - most_freq <= k

    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        charsmap = { }
        most_freq = 0
        res = 0

        while right < len(s):
            
            # Update frequency
            charsmap[s[right]] = charsmap.get(s[right], 0) + 1

            while not self.isValid(right, left,charsmap,k):
                charsmap[s[left]] = charsmap[s[left]] - 1
                left += 1
            
            res = max(res,right-left+1)

            right += 1

        return res
        