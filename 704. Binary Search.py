class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left, right):
            while left <= right:
                mid = (left+right) >>1
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid+1
                elif nums[mid] > target:
                    right = mid -1
            return -1
        return binary_search(0, len(nums) -1)
        """
    def search(self, nums: List[int], target: int) -> int:

        def binary(self, nums: List[int], target: int) -> int:
            if(len(nums) == 1): Return nums[0]

            left = binary(nums[:len(nums)])
            right = binary()
            if(target == left or target == right)
            """