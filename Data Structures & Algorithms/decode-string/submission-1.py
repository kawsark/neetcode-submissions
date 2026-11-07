# Meta: '{"felt":"medium","time":25,"help":"none","Comment":""}'
class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        for ch in s:
            if ch == ']':
                right_ops = []

                # Pop until opening bracket is found
                while st[-1] != '[':
                    right_ops.append(st.pop())
                
                # Pop the '[]' character, then construct the 
                st.pop() 
                rev_right_ops = list(reversed(right_ops))
                
                # Pop until n is completed
                left_op = ""
                while len(st) > 0 and str.isdigit(st[-1]):
                    left_op = st.pop() + left_op

                res = [''.join(rev_right_ops)] * int(left_op)
                st.extend(''.join(res))
            else:
                st.append(ch)
        
        return ''.join(st)

        