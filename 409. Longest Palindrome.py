class Solution:
    def longestPalindrome(self, s: str) -> int:
        all_freq = {} #instances of letter in dictionary
        for letter in s:
            if letter in all_freq:
                all_freq[letter] += 1
            else:
                all_freq[letter] = 1
        result = 0
        firstTime = True
        for frequency in all_freq.values():
            if frequency %2 == 0:
                result += frequency
            else:
                if firstTime:
                    result += 1
                    firstTime = False
                result += frequency-1
        return result