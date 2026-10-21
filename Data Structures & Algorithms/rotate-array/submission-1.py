class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Reverse the full array
        self.reverse(nums,0,len(nums)-1)

        # Reverse from 0 to k
        self.reverse(nums,0, (k % len(nums)) -1)

        # Reverse from k to len
        self.reverse(nums, (k % len(nums)), len(nums)-1)


    # Reverses an array in place
    def reverse(self, input: list[int], start: int, stop: int) -> None:
        i, j = start, stop
        while i < j:
            t = input[j]
            input[j] = input[i]
            input[i] = t
            j -= 1
            i += 1
        