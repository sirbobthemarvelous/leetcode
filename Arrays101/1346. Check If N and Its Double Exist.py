class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        d = {} #create dictionary / hashmap
        for val in arr:
            #greedily look for the answer in existing hashmap
            if d.get(val*2,0) or d.get(val/2,0): return True
            d[val] = 1
        return False
        """
        #using sets
        if arr.count(0) > 1: return True #multiple 0s immediate true
        S = set(arr) - {0} #remove any zeros for speed
        for i in arr:
            if 2*i in S: return True #checking the sets is faster
        return False
        
        #simple check for elements in array
        for x in arr:
            if x/2 in arr or 2*x in arr:
                return True
        return False
        """
        
        """
        hashmap = {}
        for x in range(len(arr)):
            hashmap[arr[x]] = x
            #if 2*arr[x] in hashmap.keys():
                #return True
        for x in arr:
            if 2*x in hashmap.keys():
                return True
        return False
        """


        