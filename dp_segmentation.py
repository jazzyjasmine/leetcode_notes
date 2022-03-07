class Solution139:
    # 139. Word Break
    # https://leetcode.com/problems/word-break/
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        
        max_length = max([len(word) for word in wordDict])
        
        dp[0] = True
        
        for i in range(1, len(s) + 1):
            for l in range(1, max_length + 1):
                if i < l:
                    break
                
                if not dp[i - l]:
                    continue
                    
                potential_word = s[i - l: i]
                if potential_word in wordDict:
                    dp[i] = True
                    break
                    
        return dp[len(s)]


class Solution140:
    # 140. Word Break II
    # https://leetcode.com/problems/word-break-ii/
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp = {i: [] for i in range(len(s) + 1)}
        dp[0] = 1
        
        max_len = max([len(word) for word in wordDict])
        min_len = min([len(word) for word in wordDict])
        
        word_set = set(wordDict)
        
        for i in range(1, len(s) + 1):
            for j in range(min_len, max_len + 1):
                if i < j:
                    break
                
                if not dp[i - j]:
                    continue
                
                possible_word = s[i - j: i]
                
                if possible_word in word_set:
                    if dp[i - j] == 1:
                        dp[i].append([possible_word])
                    else:
                        for lst in dp[i - j]:
                            res = lst[:]
                            res.append(possible_word)
                            dp[i].append(res)

        ans = []
        for lst in dp[len(s)]:
            ans.append(" ".join(lst))
        
        return ans