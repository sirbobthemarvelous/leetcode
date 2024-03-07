class Solution:
    def reverseString(self, s: List[str]) -> None:
        length = len(s)
        for x in range((length+1) //2):
            temp = s[x]
            s[x] = s[length-1-x]
            s[length-1-x] = temp
            
            
        """
        Do not return anything, modify s in-place instead.
        """
        