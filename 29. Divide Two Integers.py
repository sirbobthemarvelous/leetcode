class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        #base case
        if(dividend == 0 or divisor == 1): 
            return dividend
        #bit overflow stuff
        if divisor == 0 or (dividend == -2147483648 and divisor == -1):
            return 2147483647
        #check for the sign value
        sign = -1 if (dividend >0 and divisor <0) or (dividend<0 and divisor>0) else 1
        
        quotient = 0
        posDividend = abs(dividend)
        posDivisor = abs(divisor)
        #keep reaping out the dividend until its less than 1 divisor
        while(posDividend>=posDivisor):
            shift = 0
            #increase divisor magnitude as much as possible
            while(posDividend >=(posDivisor<<shift)):
                shift+=1
            #add value to the quotient
            quotient += (1 << (shift-1))
            #and remove the value from the dividend
            posDividend -= posDivisor << (shift-1)
        return -quotient if sign == -1 else quotient
                
        