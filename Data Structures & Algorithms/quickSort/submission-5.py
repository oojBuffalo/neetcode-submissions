# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        def helper(start: int, end: int):  
            if start >= end:
                return
            
            pivot = end
            swap = start

            for i in range(start, end):
                if pairs[i].key < pairs[pivot].key:
                    pairs[i], pairs[swap] = pairs[swap], pairs[i]
                    swap += 1
            
            pairs[pivot], pairs[swap] = pairs[swap], pairs[pivot]
            helper(start, swap - 1)
            helper(swap + 1, end)

        helper(0, len(pairs) - 1)
        return pairs
            