# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if not pairs:
            return []
        
        arr_states: List[List[Pair]] = [pairs.copy()]
        
        # Iterate through each array element
        for i in range(1, len(pairs)):
            j = i - 1
            
            # Insert array element into its sorted position
            while j >= 0 and pairs[j+1].key < pairs[j].key:
                temp = pairs[j+1]
                pairs[j+1] = pairs[j]
                pairs[j] = temp
                j -= 1
            
            # Append array state after each insertion    
            arr_states.append(pairs.copy())
        
        return arr_states