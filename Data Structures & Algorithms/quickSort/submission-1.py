# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.helper(pairs, 0, len(pairs) - 1)
        return pairs

    def helper(self, pairs: List[Pair], start: int, end: int):  
        # Base case: list has 1 element
        if start >= end:
            return
        
        pivot = pairs[end] # Choose pivot
        marker = start # Mark the swap position 

        # Partition list upon pivot
        for i in range(start, end):
            if pairs[i].key < pivot.key:
                temp = pairs[marker]
                pairs[marker] = pairs[i]
                pairs[i] = temp
                marker += 1
        
        # Center pivot
        pairs[end] = pairs[marker]
        pairs[marker] = pivot

        # Recurse on partitons
        self.helper(pairs, start, marker - 1)
        self.helper(pairs, marker + 1, end)
            