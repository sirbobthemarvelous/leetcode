# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        def binarySearch(left, right) -> int:
            while left < right:
                mid = (right+left) >> 1
                if(isBadVersion(mid)):
                    right = mid
                else:
                    left = mid+1
            return right
        return binarySearch(1,n)