# Meta: '{"felt":"hard","time":60,"help":"video solution"}'
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        res = [0]*len(temperatures)

        for current_index in range(len(temperatures)-1, -1, -1):
            current = temperatures[current_index]

            # Monotonic Stack: is the top element of the stack lower than current?
            while len(st) > 0 and st[-1][0] <= current:
                st.pop()
            
            if len(st) > 0:
                res[current_index] = st[-1][1] - current_index

            st.append((current,current_index))        
             
        return res

        