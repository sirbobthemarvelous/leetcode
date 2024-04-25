class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict = {} #hash map

        for n in nums1: # get the frequencies
            if n not in dict:
                dict[n] = 1
            else:
                dict[n] += 1
        result = []

        for n in nums2:
            if n in dict:
                result.append(n)
                dict[n] -= 1
                if dict[n] == 0:
                    del dict[n]
        return result
        