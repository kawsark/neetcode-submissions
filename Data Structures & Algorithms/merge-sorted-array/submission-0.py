class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m
        j = n

        for k in range(m+n, 0, -1):
            if j > 0 and nums2[j-1] > nums1[i-1]:
                nums1[k-1] = nums2[j-1]
                j -= 1
            else:
                nums1[k-1] = nums1[i-1]
                i -= 1
        
        while j > 0:
            nums1[j-1] = nums2[j-1]
            j -= 1
        

        

        