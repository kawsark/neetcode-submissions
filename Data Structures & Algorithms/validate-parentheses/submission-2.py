# Meta: '{"felt":"easy","time": 10,"help":"none"}'
class Solution:

    def isValid(self, s: str) -> bool:
        sarr = list(s)
        st = []
        opening = ['(','{','[']
        closing = [')','}',']']
        pairs = {']':'[',')':'(','}':'{'}

        for c in sarr:
            last_elem = len(st) - 1
            if c in opening:
                st.append(c)
            else:
                if last_elem < 0 or pairs[c] != st[last_elem]:
                    return False
                else:
                    st.pop()
        
        return len(st) == 0




        