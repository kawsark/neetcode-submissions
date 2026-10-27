# Meta: '{ "time": 2, "felt": east, "help": none }'
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsset = set()
        for n in nums:
            if n in numsset:
                return True
            numsset.add(n)
        
        return False
        