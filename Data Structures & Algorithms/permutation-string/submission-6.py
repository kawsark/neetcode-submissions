# Meta: '{"felt": "medium", "time": 27, "help": "claude", "Comments": "Took me some time to understand the problem. First I was rotating array"}'

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1)-1
        s1list = list(s1)
        s1list.sort()

        while r < len(s2):
            s2sub = list(s2[l:r+1])
            s2sub.sort()

            if s1list == s2sub:
                return True
            
            r += 1
            l += 1
        
        return False


        