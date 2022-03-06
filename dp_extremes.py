class Solution120:
    # 120. Triangle
    # https://leetcode.com/problems/triangle/
    """
    DP top-down
    """
    def minimumTotalTopDownDP(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        m = len(triangle[-1])
        
        # for two dimension dp array, the outer iteration should use "for" loop instead of multiplication
        # dp = [[0] * m] * n is incorrect, because of the array's reference 
        dp = [[float("inf")] * m for _ in range(n)]
        
        dp[0][0] = triangle[0][0]
        
        for i in range(1, n):
            for j in range(i + 1):
                if j - 1 < 0:
                    dp[i][j] = triangle[i][j] + dp[i - 1][j]
                else:
                    dp[i][j] = triangle[i][j] + min(dp[i - 1][j], dp[i - 1][j - 1])

        return min(dp[-1])

    """
    Memoization search
    
    O(n^2)
    
       2
      3 4
     6 5 7
    4 1 8 3
    
    Pure divide and conquer (the left subarray and right subarray are also triangle arrays) is O(2^n) because it treats the overlap node (e.g. 5) as two different nodes. Memoization search only access each node once, n(n + 1)/2 = O(n^2).
    
    For binary tree, unlike this one, the left subtree and right subtree have no overlap, so divide and conquer does not cause repeated calculation.
    """
    def minimumTotalMemoizationSearch(self, triangle: List[List[int]]) -> int:
        @lru_cache(None)
        def dfs(curr_i, curr_j):
            # the arguments must be hashable
            if curr_i == len(triangle):
                return 0

            left = dfs(curr_i + 1, curr_j)
            right = dfs(curr_i + 1, curr_j + 1)

            return min(left, right) + triangle[curr_i][curr_j]
        
        return dfs(0, 0)
    

class Solution1143:
    # 1143. Longest Common Subsequence
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for i in range(len(text1) + 1)] for j in range(len(text2) + 1)]
            
        for i in range(1, len(text2) + 1):
            for j in range(1, len(text1) + 1):
                if text2[i - 1] == text1[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[-1][-1]