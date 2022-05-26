class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s) # calculating size of string
        if (n < 2):
            return s # if string is empty then size will be 0.
                      # if n==1 then, answer will be 1(single
                      # character will always palindrome)
        start=0
        maxLength = 1
        for i in range(n):
            low = i - 1
            high = i + 1
            while (high < n and s[high] == s[i] ):                              
                high=high+1

            while (low >= 0 and s[low] == s[i] ):                
                low=low-1

            while (low >= 0 and high < n and s[low] == s[high] ):
                low=low-1
                high=high+1


            length = high - low - 1
            if (maxLength < length):
                maxLength = length
                start=low+1

        result = s[start:start + maxLength]
        return result