class Solution:
    def convert(self, s: str, numRows: int) -> str:
        #create lists for each row
        #loop through list to fill them up
        #while loop to go through string
        #if statements to check if going up or going down
        if(numRows==1):
            return s
        rows = []
        for i in range(numRows):
            rows.append("")
        whichRow = 0
        up = False
        for x in s:
            rows[whichRow] += x
            if(not up):
                whichRow+=1
                if(whichRow==numRows-1):
                    up = True
            else:
                whichRow+=-1
                if(whichRow==0):
                    up=False
        result = ""
        for i in rows:
            result+=i
        return result
                