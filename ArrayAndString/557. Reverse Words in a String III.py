class Solution:
    def reverseWords(self, s: str) -> str:
        
        #slower but less memory with lambda
        # return ' '.join(map(lambda word: word[::-1], s.split()))
        # faster but more memory with list comprehension
        # return ' '.join([i[::-1] for i in s.split()])
        words = s.split()
        words = [i[::-1] for i in s.split()]
        return ' '.join(words)
        