class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer2 = [str(x+1) for x in range(n)] #try out list comprehension
        for x in range(2, n, 3):
            answer2[x] = "Fizz"
        for x in range(4, n, 5):
            if (x+1)%3==0: answer2[x] = "FizzBuzz"
            else: answer2[x] = "Buzz"

        return answer2 
        """
        answer = ["P"] * n #initialize length of array
        #loop through and add the values 
        for x in range(n):
            if (x+1)%3 == 0: #there's probably a better way of checking divisibility, but this is the first that came to mind
                if (x+1)%5 == 0: answer[x] = "FizzBuzz"
                else: answer[x] = "Fizz"
            elif (x+1)%5 == 0: answer[x] = "Buzz"
            else: answer[x] = str(x+1)
        return answer
        """