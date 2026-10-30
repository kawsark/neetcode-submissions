class Solution:
    def calPoints(self, operations: List[str]) -> int:

        res = []

        for op in operations:
            last_index = len(res)-1
            print(f"Op is {op}")
            if op == "+":
                res.append(res[last_index] + res[last_index-1])
            elif op == "D":
                res.append(res[last_index]*2)
            elif op == "C":
                res.pop()
            else:
                res.append(int(op))
            
            print(f"res is {res}")
        
        return sum(res)

        