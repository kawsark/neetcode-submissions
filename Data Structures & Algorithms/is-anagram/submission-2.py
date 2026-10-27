# Meta: '{ "time": 2, "felt": east, "help": none }'
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_arr = list(s)
        t_arr = list(t)
        
        s_arr.sort()
        t_arr.sort()

        return s_arr == t_arr
        