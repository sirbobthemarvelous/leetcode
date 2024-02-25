class Solution:
    def countAndSay(self, n: int) -> str:
        num = "1"
        for i in range(n-1):
            new_num = ""
            for x, y in groupby(num):
        #https://www.geeksforgeeks.org/itertools-groupby-in-python/
                new_num += str(sum(1 for _ in y))+x
            num = new_num
        return num