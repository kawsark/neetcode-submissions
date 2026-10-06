class Solution:

    def calcProductExceptSelf(self, nums: List[int], k) -> int:
        m = 1
        for n in range(0,len(nums)):
            if n != k:                    
                if nums[n] == 0:
                    m = 0
                    break
                else:
                    m *= nums[n]

        return m

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        m = 1
        res = []
        for n in range(1,len(nums)):
            if nums[n] == 0:
                res = [0]*len(nums)
                res[n] = self.calcProductExceptSelf(nums,n)
                return res
            else:
                m *= nums[n]

        res.append(m)
        
        for i in range(1, len(nums)):
            if nums[i] == 0:
                c = self.calcProductExceptSelf(nums,i)
                res.append(int(c))
            else:
                r = res[i-1]/nums[i]
                r *= nums[i-1]
                res.append(int(r))
        
        return res
                

        