class Solution(object):
    def isAlienSorted(self, words, order):
        
        dict = {}
        for x,y in enumerate(order):
            dict[y] = x
            
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            
            for i in range(min(len(word1), len(word2))):
                if word1[i] != word2[i]:
                    if dict[word1[i]] > dict[word2[i]]:
                        return False
                    break
            else:
                if len(word1) > len(word2):
                    return False
        return True
        """def isEarlier(first,second): 
            for i in range(0,len(str(first))):
                if not str(first)[i] ==str(second)[i]:
                    if order.index(str(first)[i]) < order.index(str(second)[i]):
                        return True
                    else:
                        return False
                if str(second)[i] == None:
                    return False
            return True
        
        for x in range(0,len(words)-1):
            for y in range(1,len(words)):
                if not isEarlier(x,y):
                    return False
                
        return True
        """