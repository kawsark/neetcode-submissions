# Meta: '{"felt":"easy", "time": 15, "help": "minor", "comment": "to implement peek, just use last_index as len(arr)-1" }'
class Solution:
    def calPoints(self, operations: List[str]) -> int:

        res = []

        for op in operations:
            last_index = len(res)-1

            if op == "+":
                res.append(res[last_index] + res[last_index-1])
            elif op == "D":
                res.append(res[last_index]*2)
            elif op == "C":
                res.pop()
            else:
                res.append(int(op))
        
        return sum(res)

        