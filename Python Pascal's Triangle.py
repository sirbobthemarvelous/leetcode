class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        allTheLists = []
        for rowNum in range(numRows):
            allTheLists.append([])
        allTheLists[0].append(1) #first row

        for rowNumbers in range(1,numRows):
            allTheLists[rowNumbers].append(1) #the first one
            for colNumbers in range(1,len(allTheLists[rowNumbers-1])):
                allTheLists[rowNumbers].append(allTheLists[rowNumbers-1][colNumbers-1]+allTheLists[rowNumbers-1][colNumbers])
            allTheLists[rowNumbers].append(1) #the last one at the end
        return allTheLists
        
                