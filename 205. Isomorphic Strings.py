class Solution:
    def turnNum(s:str)->str:
        dict = {}
        result = ""
        index = 0
        for ele in s:
            if ele not in dict:
                index += 1
                dict[ele] = index 
            result += str(dict[ele])
        
        return result

    def isIsomorphic(self, s: str, t: str) -> bool:
        # convert string to number...dictionary?
        sNum = Solution.turnNum(s)
        tNum = Solution.turnNum(t)
        return sNum == tNum

    