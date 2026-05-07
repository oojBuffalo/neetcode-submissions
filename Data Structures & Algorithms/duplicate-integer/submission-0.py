class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen: dict[int,bool] = {}

        for num in nums:
            if num in seen:
                return True
            seen[num] = True
        
        return False

