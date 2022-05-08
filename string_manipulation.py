from collections import Counter

class Solution791:
    # 791. Custom Sort String
    # https://leetcode.com/problems/custom-sort-string/
    def customSortString(self, order: str, s: str) -> str:
        s_count = Counter(s)
        ans = [char * s_count.pop(char, 0) for char in order]
        for s_char, s_char_count in s_count.items():
            ans.append(s_char * s_char_count)
        return "".join(ans)