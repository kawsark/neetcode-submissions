# Meta: '{ "time": 25, "felt": normal, "help": none, "comment": "Solution felt clunky and required quite a bit of debugging" }'
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []
        c = 0 # Current charater being examined

        while c < len(strs[0]):
            cch = strs[0][c]
            # Check the c character of each item in strs
            for s in strs:
                if c >= len(s) or s[c] != cch:
                    return "".join(res)
                
            res.append(cch)
            c+= 1

        return "".join(res)
        