class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}

        if len(s) != len(t):
            return False


        for i in range(len(s)):
            c = s[i]
            if c in s_dict:
                s_dict[c] = s_dict[c] + 1
            else:
                s_dict[c] = 1

            d = t[i]
            if d in t_dict:
                t_dict[d] = t_dict[d] + 1
            else:
                t_dict[d] = 1

        print(s_dict)
        print(t_dict)
        
        for i in s_dict:
            if i in t_dict:
                if s_dict[i] == t_dict[i]:
                    pass
                else:
                    return False
            else:        
                return False
        
        return True