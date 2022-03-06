class Solution120:
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
    def minimumTotal(self, triangle: List[List[int]]) -> int:
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