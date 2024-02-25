class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #the best solution is to work backwards
        i = m - 1 # nums1's index
        j = n - 1 #  nums2's index
        #  a variable to store the back of the array
        k = m + n - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
            else:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1

        """
        #Slowest but most space efficient

        #alright you need to go backwards
        # 6, 5, 3, 2, 2, 1 checking that way
        index = m+n-1
        while n > 0:
            if m == 0:
                nums1[index] = nums2[n-1]

        #not too slow but not as space efficient
        x,y = 0,0
        while x < m and y < n:
            if nums1[x] >= nums2[y]:
                nums1.insert(x,nums2[y])
                y+=1
                m+=1
                nums1.pop()
            x+=1
        while y<n:
            nums1[x] = nums2[y]
            x+=1
            y+=1
        """
        
                
            
        
