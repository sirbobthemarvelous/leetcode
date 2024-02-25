class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        if not mat:return 0             #empty matrix
        m,n = len(mat),len(mat[0])      #define lengths
        res = 0
        #RLE - Run length encoding - turn aaabbbcccc into a3b3c4
        for i in range(m):
            for j in range(n):
                if j:                                   #once you get beyond the first unit...
                    if mat[i][j]:                       # and it's 1
                        mat[i][j] = mat[i][j-1] + 1     #add 1 to the previous one
                        
        #Now,calculate all the rectangular submatrices from the RLE
        print(mat)
        for i in range(m):    
            for j in range(n):
                # (i,j) :top right of matrix...or is it top left?
                ans = mat[i][j]
                for k in range(i,m):#bottom-right
                    ans = min(ans,mat[k][j])
                    res+= ans
    
        return res
"""
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        total = 0
        for m in range(1,len(mat)+1):
            for n in range(1,len(mat[0])+1):
                total += self.checkingThrough(m,n,mat)
        return total
                
    def checkingThrough(self, rows: int, cols: int, mat: List[List[int]]) -> int:
        total = 0
        
        if rows == len(mat) and cols == len(mat[0]):
            if self.checking(0,0,rows,cols,mat):
                total += 1
        elif cols == len(mat[0]):
            for startR in range(len(mat)-rows+1):
                if self.checking(startR,0,rows,cols,mat):
                    total += 1
        elif rows == len(mat):
            for startC in range(len(mat[0])-cols+1):
                if self.checking(0,startC,rows,cols,mat):
                    total += 1
        else:
            for startR in range(len(mat)-rows+1):
                for startC in range(len(mat[0])-cols+1):
                    if self.checking(startR,startC,rows,cols,mat):
                        total += 1
        
        return total
        
            
    def checking(self, startR: int, startC: int, rows: int, cols: int, mat: List[List[int]]) -> bool:
        for m in range(startR, rows+startR):
            for n in range(startC, cols+startC):
                if mat[m][n] == 0: return False
        return True
"""

# ok so this is the naive solution, how do we make it just adding one extra?