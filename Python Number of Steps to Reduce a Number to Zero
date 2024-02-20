class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0: return 0
        return num.bit_length() - 1 + num.bit_count() 
        #every odd bit is a step, and every bit shift is a step until you're down to one


        """
        count = 0
        while(num != 0):
            count+=1
            if(num%2 ==1): num-=1 #you can do num & 1 to test odd/even
            else: num/=2 #or you could do num>>=1 to be faster
        return count
        """
        