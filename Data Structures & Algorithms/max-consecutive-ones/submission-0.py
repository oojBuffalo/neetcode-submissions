class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max: int = 0
        acc: int = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                acc += 1
                if acc > max:
                    max = acc
            else:
                acc = 0
        return max