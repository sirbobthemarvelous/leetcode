class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return f"{int(a, 2)+int(b, 2):b}"
        #^ Fast overall, minimal memory
        #return "{0:b}".format(int(a, 2) + int(b, 2))
        #return str(bin(int(a, 2) + int(b,2)))[2:]
        # ^ quick but takes up space

        #this version works but is kinda slow
        array = []
        aLength = len(a)-1
        bLength = len(b)-1
        extra = 0
        while aLength >=0 or bLength >= 0 or extra: #while there's still more value to go
            if aLength >= 0:
                extra += int(a[aLength])
                aLength-=1
            if bLength >= 0:
                extra += int(b[bLength])
                bLength-=1
            array.append(str(extra%2))
            extra //=1
        return ''.join(reversed(array))
        """
        for x,y in big:
            if(x+y ==2):
                result+=extra
                extra = "1"
            elif(x+y ==0):
                result+=extra
                extra = "0"
            else:
                if(extra == "1"):
                    extra = "0"
                    result+=extra
                else:
                    extra = "1"
                    result+=extra

        return reverse(result)
        """