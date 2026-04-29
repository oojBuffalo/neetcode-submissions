class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n: int = len(arr)  # Length of array

        for i in range(n):
            if i == n-1:
                arr[i] = -1
                break
            arr[i] = max(arr[i+1:])

        return arr