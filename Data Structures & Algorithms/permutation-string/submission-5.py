class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1)-1
        s1sub = list(s1)
        s1sub.sort()

        while r < len(s2):
            s2sub = list(s2[l:r+1])
            s2sub.sort()
            #print(f"Checking {s1sub} == {s2sub}")

            if s1sub == s2sub:
                return True
            
            r += 1
            l += 1
        
        return False


        