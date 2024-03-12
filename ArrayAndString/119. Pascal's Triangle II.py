class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]
        elif rowIndex==1:
            return [1,1]
        
        result=[[1],[1,1]]
        
        
        for i in range(1,rowIndex):
            generate=[0]*(len(result[i])+1)
            
            generate[0],generate[-1]=1,1
            for j in range(1,len(generate)-1):
                generate[j]=result[i][j-1]+result[i][j]
            result.append(generate)
            
        return result[-1]
        
        """
        #rework old version
        allTheLists = []
        for rowNum in range(rowIndex+1):
            allTheLists.append([])
        allTheLists[0].append(1) #first row

        for rowNumbers in range(1,rowIndex+1):
            allTheLists[rowNumbers].append(1) #the first one
            for colNumbers in range(1,len(allTheLists[rowNumbers-1])):
                allTheLists[rowNumbers].append(allTheLists[rowNumbers-1][colNumbers-1]+allTheLists[rowNumbers-1][colNumbers])
            allTheLists[rowNumbers].append(1) #the last one at the end
        return allTheLists[rowIndex]
        """



        