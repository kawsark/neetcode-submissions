class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n
        postfix = [0] * n
        res = [0] * n
    
        prefix[0] = nums[0]
        postfix[n-1] = nums[n-1]
        
        for i in range(1,n):
            prefix[i] = prefix[i-1]*nums[i]

        for j in range(n-2, -1, -1):
            postfix[j] = postfix[j+1]*nums[j]

        res[0] = postfix[1]
        res[n-1] = prefix[n-2]

        for i in range(1,n-1):
            res[i] = prefix[i-1]*postfix[i+1]

        return res

        