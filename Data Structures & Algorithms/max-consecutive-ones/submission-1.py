class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max: int = 0       # Max number of consecutive ones
        acc: int = 0       # Accumulator var for counting
        n: int = len(nums) # Length of array

        for i in range(n):
            if nums[i] == 1:
                acc += 1
                if acc > max:
                    max = acc
            else:
                acc = 0

        return max