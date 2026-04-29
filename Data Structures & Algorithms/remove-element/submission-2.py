class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n: int = len(nums) # Length of array
        j: int = 0         # Write index for loop

        for i in range(n):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1

        return j