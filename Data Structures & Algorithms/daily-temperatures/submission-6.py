# Meta: '{"felt":"medium","time":30,"help":"None", "comment": "Whether it is sorted ascending or descending is tricky, and whether to pop or push equal temps are tricky"}'
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        st = []

        for i in range(len(temperatures)-1,-1,-1):
            t = temperatures[i]
            while len(st) > 0 and st[-1][0] <= t:
                st.pop()
            
            st.append((t,i))
            
            if len(st) > 1:
                res[i] = st[-2][1] - i

        return res

                
            

            



        