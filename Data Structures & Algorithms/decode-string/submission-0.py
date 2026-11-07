class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        sarr = list(s)
        for ch in sarr:
            if ch == ']':
                right_ops = []

                # Pop until opening bracket is found
                while True:
                    op = st.pop()
                    if op == '[':
                        break
                    else:
                        right_ops.append(op)
                
                rev_right_ops = [0] * len(right_ops)
                idx = len(right_ops) - 1
                for r in right_ops:
                    rev_right_ops[idx] = r
                    idx -= 1
                
                # Pop until n is completed
                left_op = ""
                while True:
                    if len(st) > 0 and str.isdigit(st[-1]):
                        op = st.pop()
                        left_op = op + left_op
                    else:
                        break

                res = [''.join(rev_right_ops)] * int(left_op)
                st.extend(''.join(res))
            else:
                st.append(ch)
        
        return ''.join(st)

        