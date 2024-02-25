class Solution:
    def rob(self, nums: List[int]) -> int:
        # bottomup approach
        def specrob(arr,currindex):
            t=[0]*(len(arr)+2)
            for i in range(len(arr)-1,-1,-1):
                t[i]=max(arr[i]+t[i+2],t[i+1])
            return t[0] 
            # here from last to we are coming first so result stored in forst index
        return specrob(nums,0)