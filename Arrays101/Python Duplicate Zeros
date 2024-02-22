class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        x = 0
        while x < len(arr)-1:
            if arr[x] == 0:
                arr.insert(x,0)
                arr.pop()
                x += 1
            x+=1
        