class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        result = []
        wordSet = set(wordDict)

        def backtrack(curr, okk):
            if len(okk) == 0:
                result.append(curr.strip())
                return

            for i in range(len(okk)):
                lstr = okk[:i + 1]
                if lstr in wordSet:
                    rstr = okk[i + 1:]
                    if curr:
                        backtrack(curr + " " + lstr, rstr)
                    else:
                        backtrack(lstr, rstr)

        backtrack("", s)
        return result