class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        "create empty array"
        size = len(nums1)+len(nums2)
        combined = [0]* size
        "sort 2 arrays into order by comparing 1 by 1"
        "return the middle of the array"
        one = 0
        two = 0
        for i in range(size):
            if(one >= len(nums1)):
                combined[i] = nums2[two]
                two+=1
            elif(two >= len(nums2)):
                combined[i] = nums1[one]
                one+=1
            elif(nums1[one]<nums2[two]):
                combined[i] = nums1[one]
                one+=1
            else:
                combined[i] = nums2[two]
                two+=1
                
        if(size%2 == 0):
            return ((combined[int(size/2)]+combined[int(size/2) -1])/2)
        else:
            return combined[int(size/2)]