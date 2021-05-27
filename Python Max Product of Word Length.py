class Solution(object):
    def maxProduct(self, words):
        unique = 0
        def checkDuplicateChar(first, second):
            for letter in first:
                for letter2 in second:
                    if letter == letter2:
                        return True
            return False
        
        for index, value in enumerate(words):
            for index2, value2 in enumerate(words):
                if(index < index2): 
        #behold the ability to compare things in an array with enumerate
                    if(len(value)*len(value2) > unique):
                        #sets are arrays of all the Unique characters
                        setting = set(value)
                        setting2 = set(value2)
                        if(checkDuplicateChar(setting,setting2)==False):
                            unique = len(value)*len(value2)

        return unique