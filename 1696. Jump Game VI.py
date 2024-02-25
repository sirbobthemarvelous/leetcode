class Solution:
	def maxResult(self, nums: List[int], k: int) -> int:
		n = len(nums)
		deq = deque([n-1])
		for i in range(n-2, -1, -1):
			if deq[0] - i > k: deq.popleft()
			nums[i] += nums[deq[0]]
			while len(deq) and nums[deq[-1]] <= nums[i]: deq.pop()
			deq.append(i)
		return nums[0]
		
		"""
        #alright so let's recursively work backwards
        #make an array of the potential number of steps you can take
        options = []
        for choice in range(0,k):
            options.append(nums[len(nums)-1-choice])
    
        total = 0
        leg = len(nums)-1
        #loop through the list backwards
        while True:
            if leg==0:
                break
            total+= max(options)
            
            #and to shift the options to the new paradigm
            for shiftAmount in range(0,k):
                
                leg+=1
                #shift individual indexes once
                for oneTime in options:
                    if oneTime == options[len(options)-1]:
                        options[oneTime]=nums[len(nums)-1-oneTime-leg]
                    else:
                        options[oneTime]=options[oneTime+1]
                        
                #ughhhh but I have to also make sure the out of bounds stuff doesn't happen
                
                #keep shifting until you hit the distance
                if max(options)==options[shiftAmount]:
                    break
            
        # then repeat until you reach the beginning
        return total
        """