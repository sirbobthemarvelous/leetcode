class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #XOR is faster
        result = 0
        for num in nums:
            result ^= num
        return result

        #hashset works but it's slow
        hashset = set()
        for x in nums:
            if x in hashset:
                hashset.remove(x)
            else:
                hashset.add(x)
        return list(hashset)[0]
        