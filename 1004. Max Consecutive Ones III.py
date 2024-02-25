class Solution(object):
    def longestOnes(self, A, K):
        i=0;n=len(A);j=0
        countk=K;res=float('-inf')
        while j<n and i<n:
            if A[j]==1:
                pass
            else:   
                if countk>0:
                    countk-=1
                else:
                    while countk<0 or A[i]==1:
                        if A[i]==0:
                            countk+=1
                        i+=1
                    i+=1
            res=max(res,j-i+1)  
            j+=1
        return res 
        