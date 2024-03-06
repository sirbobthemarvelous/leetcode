class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        height = len(mat)
        width = len(mat[0])
        if(height == 1): return mat[0]

        result = []
        if(width ==1):
            for x in mat:
                result.append(x[0])
            return result

        index = 0 #up and down
        index2 = 0 #left and right
        upperRight = True
        
        for x in range(height * width):
            result.append(mat[index][index2])

            if(upperRight): #keep going upRight until you hit the ceiling or the right wall.
                if(index2 == width-1): #hitting the right wall
                    index+=1
                    upperRight = False
                elif(index == 0): #hitting the ceiling 
                    index2+=1 
                    upperRight = False
                else: #the normal movement
                    index-=1
                    index2+=1

            else: #downLeft until you hit the floor or left wall
                if(index == height-1): #you hit the floor 
                    index2 +=1
                    upperRight = True
                elif(index2 ==0): #hitting the left wall 
                    index+=1 
                    upperRight = True
                else: #the normal movement
                    index+=1
                    index2-=1
        return result



        