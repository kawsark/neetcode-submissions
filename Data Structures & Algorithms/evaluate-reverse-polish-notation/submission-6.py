# Meta: '{"felt": "easy", "time": 10, "help": "none"}'
class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        ops = ['+', '-', '*', '/']

        for op in tokens:
            if op in ops:
                r = st.pop()
                l = st.pop()
                res = None
                
                if op == "+":
                    res = l+r
                elif op == "-":
                    res = l-r
                elif op == "*":
                    res = l*r
                else:
                    res = int(l/r)
                
                st.append(res)
            else:
                st.append(int(op))
        
        return st.pop()

        