class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def update(self, index: int, val: int) -> None:
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        #for loop too slow use sum method
        return sum(self.nums[left:right+1])
#https://lenchen.medium.com/leetcode-307-range-sum-query-mutable-8d1774977778
# the Quick solution

