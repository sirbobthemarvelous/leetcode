
from collections import Counter
import string
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        rmPunctuation = str.maketrans(string.punctuation, ' '*len(string.punctuation))
        #rmPunctuation = str.maketrans('','',string.punctuation)
        # remove punctuation, lowercase it, split into words
        split_ver = paragraph.translate(rmPunctuation).lower().split()

        #remove banned
        for j in banned:
            split_ver = [i for i in split_ver if i != j]
        
        #put the split data into the Counter class, grab most common, grab the key value
        #return Counter(split_ver).most_common(10)
        return Counter(split_ver).most_common(1)[0][0]
        
