from typing import List

class Solution523:
    # 523. Continuous Subarray Sum
    # Time: O(n), Space: O(k)
    # not dp, using mod math instead
    # running sum at index i = a
    # running sum at index j (j - i > 1) = b
    # b - a = d 
    # if True, d % k == 0 =>(b - a) % k == 0 => b % k - a % k == 0 => b % k == a % k
    # reference: https://leetcode.com/problems/continuous-subarray-sum/discuss/150330/Math-behind-the-solutions
    # https://leetcode.com/problems/continuous-subarray-sum/
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        seen_mod_to_index = {0: -1}  # don't forget initial value
        cum_sum = 0  # cumulative sum
        for i in range(len(nums)):
            cum_sum += nums[i]
            curr_mod = cum_sum % k
            if curr_mod in seen_mod_to_index:
                if i - seen_mod_to_index[curr_mod] > 1:
                    # make sure the subarray has length at least 2
                    return True
            else:
                # ! only update dictionary when a new mod is met
                # for each mod (key), keep its value the left-most index, not right-most
                seen_mod_to_index[curr_mod] = i
        return False
        