from typing import List

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # Create a list of sets of characters for each word
        char_sets = [set(word) for word in words]
        
        max_product = 0
        n = len(words)
        for i in range(n):
            for j in range(i + 1, n):
                # If the character sets of two words have no intersection (no common characters)
                if not char_sets[i].intersection(char_sets[j]):
                    # Calculate the product of their lengths
                    product = len(words[i]) * len(words[j])
                    max_product = max(max_product, product)
        return max_product
"""
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
"""