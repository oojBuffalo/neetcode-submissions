class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n: int = len(nums) # Length of array
        i: int = 0         # Read index for loop
        j: int = 0         # Write index for loop

        for i in range(n):
            if nums[i] == val:
                continue
            else:
                nums[j] = nums[i]
                j += 1

        # The number of remaining elements is equal to the next write index
        #     i.e. num elements written + 1 = next write index
        return j