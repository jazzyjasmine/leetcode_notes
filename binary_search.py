from typing import List


class Solution1060:
    # 1060. Missing Element in Sorted Array
    # Note that the numbers are in ascending order and unique
    # The cumulative missing count for each index is also in ascending order
    # E.g. [4,7,9,10], the corresponding cumulative missing count is [0,2,3,3]
    # The cumulative missing count for each index can be computed in O(1): nums[index] - (nums[0] + index)
    # Target: Find the first index (from left) whose cumulative missing count >= k
    # https://leetcode.com/problems/missing-element-in-sorted-array/
    def missingElement_binary_search(self, nums: List[int], k: int) -> int:
        # Time O(lgn), Space O(1)
        missing = lambda index: nums[index] - (nums[0] + index)
        left, right = 0, len(nums) - 1
        
        while left + 1 < right:
            mid = left + (right - left) // 2
            if missing(mid) >= k:
                right = mid
            else:
                left = mid
        
        target = len(nums) - 1
        if missing(left) >= k:
            target = left - 1
        
        elif missing(right) >= k:
            target = right - 1
        
        return nums[target] + k - missing(target)
    
    def missingElement_one_pass(self, nums: List[int], k: int) -> int:
        # Time O(n), Space O(1)
        prev_missing, total_missing = 0, 0
        for i in range(1, len(nums)):
            total_missing += nums[i] - nums[i - 1] - 1
            
            if total_missing >= k:
                return nums[i - 1] + k - prev_missing
            
            prev_missing = total_missing
        
        return nums[-1] + k - total_missing
