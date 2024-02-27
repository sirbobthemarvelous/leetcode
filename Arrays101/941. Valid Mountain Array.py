class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        max_num = max(arr)
        # Edge cases --> if the slope of the mountain is strictly increasing/decreasing
        if max_num == arr[len(arr) - 1] or max_num == arr[0]:
            return False
        max_found = False
        for i in range(len(arr) - 1):
            # We initially want the mountain to be increasing but
            # once we find the max number, we want the mountain to decrease
            if arr[i] == max_num:
                max_found = True
            if max_found and arr[i] <= arr[i + 1]:
                return False
            elif not max_found and arr[i] >= arr[i + 1]:
                return False
        return True
"""
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3: return False
        if arr[1] < arr[0]: return False
        ascending = True
        for x in range(1,len(arr)):
            if(arr[x] == arr[x-1]): return False
            if(ascending and arr[x] < arr[x-1]): ascending = False
            if(not ascending and arr[x] > arr[x-1]): return False
        return not ascending 
"""

        