class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #just checking the length is faster but more memory
        return len(set(nums))!=len(nums)
        #hashsets don't use much memory but it's not fast
        hashset = set()
        for x in nums:
            if x in hashset:
                return True
            else:
                hashset.add(x)
        return False
        