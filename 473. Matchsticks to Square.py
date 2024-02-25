class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or len(nums) < 4:
            return False;

        sum_len = sum(nums)
        if sum_len % 4 != 0:
            return False

        # The reason we sort and reverse nums is that
        # in the recursion, 
        # if each time we can try the longer matchstick first, 
        # then the bad solution will quit the pipe 'or' statement earlier.
        nums.sort()
        nums.reverse()

        border_len = sum_len / 4
        sums = [0 for _ in xrange(4)]

        return self.makesquare_helper(nums, 0, sums, border_len)

    def makesquare_helper(self, nums, index, sums, border_len):
        # base case
        if sums[0] > border_len or sums[1] > border_len or sums[2] > border_len or sums[3] > border_len:
            return False

        if index >= len(nums):
            if sums[0] == sums[1] == sums[2] == sums[3] == border_len:
                return True
            return False

        n = nums[index]
        for i in xrange(4):
            if sums[i] + n > border_len:
                continue

            sums[i] += n

            # recursion.
            if self.makesquare_helper(nums, index + 1, sums, border_len):
                return True

            sums[i] -= n

        return False
        