class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = len(nums)
        k = 0
        i = 0
        while i < l:
            print(f"[{i}] {nums}")

            if nums[i] == val:
                nums.pop(i)
                nums.append(val)
                l -= 1
                i -= 1
            else:
                k += 1

            i += 1

            print(f"[{i}] {nums}")
            print("@@@")


        return k
        