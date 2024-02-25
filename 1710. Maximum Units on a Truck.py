class Solution:
    def maximumUnits(self, boxTypes, truckSize):
        boxTypes.sort(key=lambda x: -x[1])
        ans = 0
        for t, u in boxTypes:
            if truckSize > t:
                truckSize -= t
                ans += t * u
            else:
                ans += truckSize * u
                return ans
        return ans
        """
        #sorting algorithm for the box type capacity
        #algorithm looks for largest box type and puts it to the front
        maximum = 0
        for biggest in range(0,len(boxTypes)-1):
            for thickest in range(0,len(boxTypes)-1):
                if boxTypes[thickest][1] < boxTypes[thickest+1][1]:
                    maximum = thickest+1
            boxTypes.insert(biggest,boxTypes.pop(maximum))
 
        units = 0
        #and then keep adding until you hit the box limit
        while truckSize>0:
            if boxTypes[0][0] == 0:
                boxTypes.pop(0)
                continue
            units += boxTypes[0][1]
            boxTypes[0][0] += -1
        return units
        """