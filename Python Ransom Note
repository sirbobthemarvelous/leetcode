class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #using counters isn't faster it's just cleaner
        st1, st2 = Counter(ransomNote), Counter(magazine)
        if st1 & st2 == st1:
            return True
        return False
        """
        dictionary = {}
        for letter in magazine:
            if(letter in dictionary): 
                dictionary[letter] += 1
            else:
                dictionary[letter] = 1
        for letter in ransomNote:
            if(letter in dictionary and dictionary[letter] > 0): 
                dictionary[letter] -= 1
            else:
                return False
        return True
        """


        