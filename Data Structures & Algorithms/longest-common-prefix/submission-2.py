class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]
        res = ""
        for i in list(first):
            res = res + i
            for j in range(1,len(strs)):
                if not strs[j].startswith(res):
                    return res[:-1]
        
        return res


        