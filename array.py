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


class Solution670:
    # 670. Maximum Swap
    # Summary: one change to maximize the number
    # https://leetcode.com/problems/maximum-swap/
    # Idea: Scan the array from right to left, keep track of the global max digit,
    # if a digit is less than the current global max digit, record the digit itself (position)
    # into "change_pos" and record the current global max digit (position) into "change_max_pos"
    def maximumSwap(self, num: int) -> int:
        list_num = [int(i) for i in str(num)]
        
        max_pos = len(list_num) - 1  # global max position
        
        change_pos = 0  # left-most digit that is smaller than the max digit to its right
        change_max_pos = 0  # the max digit to the change_pos's right
        
        for pos in range(len(list_num) - 1, -1, -1):
            if list_num[pos] > list_num[max_pos]:
                max_value = list_num[pos]
                max_pos = pos
            elif list_num[pos] < list_num[max_pos]:
                change_pos = pos
                change_max_pos = max_pos
        
        list_num[change_pos], list_num[change_max_pos] = list_num[change_max_pos], list_num[change_pos]
        
        return int("".join([str(x) for x in list_num]))


class Solution498:
    # 498. Diagonal Traverse
    # Simulation
    # https://leetcode.com/problems/diagonal-traverse/
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        up = True
        i, j = 0, 0
        ans = []
        while self.isValid(mat, i, j):
            ans.append(mat[i][j])
            i, j, up = self.getNextStep(mat, i, j, up)
        return ans
    
    def getNextStep(self, mat, i, j, up):
        if up:
            ni, nj = i - 1, j + 1
            if not self.isValid(mat, ni, nj):
                up = False
                ni, nj = i, j + 1
                if not self.isValid(mat, ni, nj):
                    ni, nj = i + 1, j
        else:
            ni, nj = i + 1, j - 1
            if not self.isValid(mat, ni, nj):
                up = True
                ni, nj = i + 1, j
                if not self.isValid(mat, ni, nj):
                    ni, nj = i, j + 1
        return (ni, nj, up) if self.isValid(mat, ni, nj) else (-1, -1, up)
    
    def isValid(self, mat, ni, nj):
        return 0 <= ni < len(mat) and 0 <= nj < len(mat[0])
