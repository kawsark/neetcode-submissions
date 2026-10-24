class Solution:
   def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        sub = set()
        res = 0
        # a
        for r in range(len(s)):
            while s[r] in sub: # Need to go past the repeated character
               res = max(res,len(sub))
               sub.remove(s[l])
               l += 1
            
            sub.add(s[r])
        
        res = max(res,len(sub))

        return res
