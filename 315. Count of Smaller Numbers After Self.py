class FenwickTree:
  def __init__(self, n: int):
    self.sums = [0] * (n + 1)

  def update(self, i: int, delta: int) -> None:
    # update the i-th element in the Fenwick tree with delta
    while i < len(self.sums):
      self.sums[i] += delta
      i += FenwickTree.lowbit(i)

  def get(self, i: int) -> int:
    # get the sum of the first i elements in the Fenwick tree
    summ = 0
    while i > 0:
      summ += self.sums[i]
      i -= FenwickTree.lowbit(i)
    return summ

  @staticmethod
  def lowbit(i: int) -> int:
    # get the lowest set bit in the binary representation of i
    return i & -i


class Solution:
  def countSmaller(self, nums: List[int]) -> List[int]:
    ans = []
    ranks = collections.Counter()
    # get the rank of each unique element in nums
    self._getRanks(nums, ranks)
    tree = FenwickTree(len(ranks))

    # iterate through nums backwards
    for num in reversed(nums):
      # get the number of elements smaller than num that have been seen so far
      ans.append(tree.get(ranks[num] - 1))
      # update the rank of num in the Fenwick tree
      tree.update(ranks[num], 1)

    # reverse the answer since we iterated backwards through nums
    return ans[::-1]

  def _getRanks(self, nums: List[int], ranks: Dict[int, int]) -> None:
    rank = 0
    # iterate through the sorted set of unique elements in nums
    for num in sorted(set(nums)):
      # assign a rank to each unique element
      rank += 1
      ranks[num] = rank