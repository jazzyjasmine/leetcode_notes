class SparseVector1570:
    # 1570. Dot Product of Two Sparse Vectors
    # https://leetcode.com/problems/dot-product-of-two-sparse-vectors/
    def __init__(self, nums: List[int]):
        self.zeros_positions = set()
        self.positions = set()
        for index, num in enumerate(nums):
            self.positions.add(index)
            if num == 0:
                self.zeros_positions.add(index)
        self.vector = nums[:]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        zeros = self.zeros_positions | vec.zeros_positions
        non_zeros_pos = self.positions - zeros
        ans = 0
        for pos in non_zeros_pos:
            ans += self.vector[pos] * vec.vector[pos]
        return ans