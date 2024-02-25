class Solution:
    def checkEverything(self, naanbinary: List[str], backCheck: str, openPar: int, closePar: int, n: int) -> None:
        #Victory Case
        if openPar == n and closePar == n:
            naanbinary.append(backCheck)
            return
            
        #when open parantheses are less than required
        if openPar < n:
            self.checkEverything(naanbinary, backCheck+"(", openPar +1, closePar, n)
                
        #when we need more close parentheses to balance
        if closePar < openPar:
            self.checkEverything(naanbinary, backCheck + ")", openPar, closePar+1,n)
        
    def generateParenthesis(self, n: int) -> List[str]:
        naanbinary = [] #behold a list
        
        
        self.checkEverything(naanbinary, "", 0,0,n)
        return naanbinary
            
        

        
        