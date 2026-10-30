# Meta: '{"felt":"easy", "time": 15, "help": "minor", "comment": "to implement peek, just use last_index as len(arr)-1" }'
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for ops in operations:
            last_index = len(res)-1

            if ops == "+":
                res.append(res[last_index] + res[last_index-1])
            elif ops == "D":
                res.append(res[last_index]*2)
            elif ops == "C":
                res.pop()
            else:
                res.append(int(ops))
        
        return sum(res)

        