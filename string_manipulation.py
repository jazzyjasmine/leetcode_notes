from collections import Counter

class Solution408:
    # 408. Valid Word Abbreviation
    # https://leetcode.com/problems/valid-word-abbreviation/
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word_ptr, abbr_ptr = 0, 0
        while abbr_ptr < len(abbr) and word_ptr < len(word):
            if not abbr[abbr_ptr].isnumeric():
                if word[word_ptr] == abbr[abbr_ptr]:
                    word_ptr += 1
                    abbr_ptr += 1
                    continue
                else:
                    return False
            
            if abbr[abbr_ptr] == '0':
                return False
            
            start = abbr_ptr
            while abbr_ptr < len(abbr) and abbr[abbr_ptr].isnumeric():
                abbr_ptr += 1
            number = int(abbr[start:abbr_ptr])
            word_ptr += number
        
        return word_ptr == len(word) and abbr_ptr == len(abbr)


class Solution791:
    # 791. Custom Sort String
    # https://leetcode.com/problems/custom-sort-string/
    def customSortString(self, order: str, s: str) -> str:
        s_count = Counter(s)
        ans = [char * s_count.pop(char, 0) for char in order]
        for s_char, s_char_count in s_count.items():
            ans.append(s_char * s_char_count)
        return "".join(ans)