import collections

class Solution423:
    # 423. Reconstruct Original Digits from English
    # https://leetcode.com/problems/reconstruct-original-digits-from-english/
    def originalDigits(self, s: str) -> str:
        count = collections.Counter(s)
        
        digit_to_times = {}
        
        digit_to_times['0'] = count['z']
        digit_to_times['2'] = count['w']
        digit_to_times['4'] = count['u']
        digit_to_times['6'] = count['x']
        digit_to_times['8'] = count['g']
        
        digit_to_times['3'] = count['h'] - digit_to_times['8']
        digit_to_times['5'] = count['f'] - digit_to_times['4']
        digit_to_times['7'] = count['s'] - digit_to_times['6']
        
        digit_to_times['9'] = count['i'] - digit_to_times['5'] - digit_to_times['6'] - digit_to_times['8']
        digit_to_times['1'] = count['n'] - digit_to_times['7'] - digit_to_times['9'] * 2  # note that 9 takes up two 'n's
        
        result_list = [key * digit_to_times[key] for key in sorted(digit_to_times)]
        
        return "".join(result_list)
        