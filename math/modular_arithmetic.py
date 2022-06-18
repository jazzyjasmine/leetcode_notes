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


class Solution1010:
    # 1010. Pairs of Songs With Total Durations Divisible by 60
    # Time: O(n); Space: O(1) because the hashmap length is O(60)
    # (a + b) mod c == 0 => (a mod c + b mod c) mod c == 0
    # if b mod c == 0, then a mod c == 0 because a mod c is in range [0, c) so it can only be 0 since it can not be c.
    # if b mod c != 0, then a mod c + b mod c == c, because since b mod c is not 0, a mod c + b mod c can not be 0, and it can not be 2c because a mod c is in range [0, c) and b mod c is in range [0, c). Therefore the addition can only be c.
    # Key to understand the arithmetic: The range of a % c is [0, c)
    # https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
    # reference: https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/solution/
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainder_to_count = {key: 0 for key in range(60)}
        pair_count = 0
        for duration in time:
            remainder = duration % 60
            if remainder == 0:
                pair_count += remainder_to_count[0]
            else:
                pair_count += remainder_to_count[60 - remainder]
            remainder_to_count[remainder] += 1
        return pair_count
 