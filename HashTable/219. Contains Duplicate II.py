class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict = {} #hash map

        index = 0
        while(index < len(nums)):
            if(nums[index] not in dict):
                dict[nums[index]] =index #keep track of the indexes
            else:
                if -k <= (dict[nums[index]]-index) <= k:
                    return True #find the duplicate
                dict[nums[index]] =index #update the index
            index += 1
        
        return False