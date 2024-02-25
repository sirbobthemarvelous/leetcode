class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #sliding window to Substring with same set of freq of chars
        ans = []
        #store_s: Store frequency of characters in s
        #store_p: Store frequency of characters in p
        store_s, store_p = [0] *26, [0]*26
        n,m = len(s), len(p)
        j = 0
        #count frequency of characters in p
        for x in p:
            store_p[ord(x) - ord('a')] += 1
        for i in range(n):
            #add s[j] to the window if the window isn't full
            while j< n and j-i+1 <= m:
                store_s[ord(s[j]) - ord('a')] += 1
                j+= 1
            #check if both frequencies matches
            if store_s == store_p:
                # i is the starting index of the window
                ans.append(i)
            #remove the leftmost element from the window
            store_s[ord(s[i])-ord('a')] -= 1
        return ans
        