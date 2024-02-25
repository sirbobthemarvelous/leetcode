# This isn't a fast or simple solution, but it's one I came up with myself
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        index = 0
        found = True
        if nums[0] >= 0: found = False # no need to split
        if nums[len(nums)-1] < 0: #all negative
            found = False
            nums.reverse()

        if found:
            #get the entire negative line
            for x in nums:
                if x >= 0:
                    break
                index+=1
            neg = nums[:index:]
            neg.reverse() #reverse the order
            pos = nums[index::]
            #merge the two lists
            indexNeg, indexPos = 0, 0
            answer = []
            for y in range(len(nums)):
                if indexNeg == len(neg): 
                    answer.extend(pos[indexPos::])
                    break
                elif indexPos == len(pos):
                    answer.extend(neg[indexNeg::])
                    break
                elif pos[indexPos] < abs(neg[indexNeg]):
                    answer.append(pos[indexPos])
                    indexPos+=1
                else:
                    answer.append(neg[indexNeg])
                    indexNeg+=1
            answer = map(lambda x: x*x, answer) #square the list
            return list(answer)
            

        nums = map(lambda x: x*x, nums) #square the list
        return list(nums)

"""
Other solutions

built-in sort
    def sortedSquares(self, A: List[int]) -> List[int]:
        for i in range(len(A)):
            A[i] *= A[i]
        A.sort()
        return A
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted([v**2 for v in A])
    def sortedSquares(self, A: List[int]) -> List[int]:
        return_array = [v**2 for v in A]
		return_array.sort() # This is in place!
		return return_array

Raw Pointers (The Fastest)
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return_array = [0] * len(A)
        write_pointer = len(A) - 1
        left_read_pointer = 0
        right_read_pointer = len(A) - 1
        left_square = A[left_read_pointer] ** 2
        right_square = A[right_read_pointer] ** 2
        while write_pointer >= 0:
            if left_square > right_square:
                return_array[write_pointer] = left_square
                left_read_pointer += 1
                left_square = A[left_read_pointer] ** 2
            else:
                return_array[write_pointer] = right_square
                right_read_pointer -= 1
                right_square = A[right_read_pointer] ** 2
            write_pointer -= 1
        return return_array
Deque (Pretty and fast)
    def sortedSquares(self, A: List[int]) -> List[int]:
        number_deque = collections.deque(A)
        reverse_sorted_squares = []
        while number_deque:
            left_square = number_deque[0] ** 2
            right_square = number_deque[-1] ** 2
            if left_square > right_square:
                reverse_sorted_squares.append(left_square)
                number_deque.popleft()
            else:
                reverse_sorted_squares.append(right_square)
                number_deque.pop()
        return reverse_sorted_squares[::-1]

Using Generator Functions
class Solution:
    
    def generate_sorted_squares(self, nums):
        
        # Start by doing our binary search to find where
        # to place the pointers.
        left = 0
        right = len(nums)
        while right - left > 1:
            mid = left + (right - left) // 2
            if nums[mid] > 0:
                right = mid
            else:
                left = mid
        
        # And now the main generator loop. The condition is the negation
        # of the StopIteration condition for the iterator approach.
        while left >= 0 or right < len(nums):
            if left < 0:
                right += 1
                yield nums[right - 1] ** 2
            elif right >= len(nums):
                left -= 1
                yield nums[left + 1] ** 2
            else:
                left_square = nums[left] ** 2
                right_square = nums[right] ** 2
                if left_square < right_square:
                    left -= 1
                    yield left_square
                else:
                    right += 1
                    yield right_square
        
    
    def sortedSquares(self, A: List[int]) -> List[int]:
        return list(self.generate_sorted_squares(A))