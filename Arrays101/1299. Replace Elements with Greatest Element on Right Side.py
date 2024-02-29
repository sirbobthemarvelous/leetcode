class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        if len(arr) == 1: 
            arr[len(arr)-1] = -1
            return arr
        largest = arr[len(arr)-1]
        arr[len(arr)-1] = -1
        for x in range(len(arr)-2,-1,-1):
            if arr[x] > largest:
                temp = arr[x]
                arr[x] = largest
                largest = temp
            else:
                arr[x] = largest

        return arr

        """
        #Simpler notation, not much faster
        m = -1
        for i in range(len(arr)-1,-1,-1):
            if arr[i]>m :
                m, arr[i] = arr[i], m
            else:
                arr[i] = m
        return arr
        """
        

        