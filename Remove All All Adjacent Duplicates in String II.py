"""
1209. Remove All Adjacent Duplicates in String II
Given a string s, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them causing the left and the right side of the deleted substring to concatenate together.
We repeatedly make k duplicate removals on s until we no longer can.
Return the final string after all such duplicate removals have been made.
"""

class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        removelist = list()
        list2 = list(s)
        DuplicatesFound = 0
        while True:
            for x in range(0,len(s)-1):
                for y in range(x,x+k-1):
                    if list2[x] != list2[y]:
                        break
                    if y == x+k-1:
                        DuplicatesFound += 1
                        for z in range(x,x+k-1):
                            removelist.append(z)
            for target in reversed(removelist):
                list2.pop(target)
            removelist.clear()
            if DuplicatesFound == 0:
                return s
            DuplicatesFound == 0
                        
        