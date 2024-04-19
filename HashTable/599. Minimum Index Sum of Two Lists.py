class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dict = {} #hash map
        for i,n in enumerate(list1):
            if n not in dict:
                dict[n] = i #store the index of list 1
        smallest = []
        smallVal = 2000
        for i,n in enumerate(list2):
            if n in dict:
                if dict[n]+i < smallVal: #greedily check for the smallest
                    smallVal = dict[n]+i
                    smallest = []
                    smallest.append(n)
                elif dict[n]+i == smallVal:
                    smallest.append(n)
        return smallest