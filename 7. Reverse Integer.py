class Solution:
    def reverse(self, x: int) -> int:
        #transform into string
        #if negative sign, keep it, if not, reverse subsequence
        x = str(x)
        if x[0] == '-':
            a = int('-' + x[-1:0:-1])
            if a >= -2147483648 and a<= 2147483647:
                return a
            else:
                return 0
        else:
            a = int(x[::-1])
            if a >= -2147483648 and a<= 2147483647:
                return a
            else:
                return 0