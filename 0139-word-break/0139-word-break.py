class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        result = []
        wordSet = set(wordDict)
        hii = {}

        def backtrack(curr, okk):
            if okk in hii:
                return hii[okk]

            if len(okk) == 0:
                result.append(curr.strip())
                return True

            for i in range(len(okk)):
                lstr = okk[:i + 1]

                if lstr in wordSet:
                    rstr = okk[i + 1:]

                    if backtrack(curr + "," + lstr, rstr):
                        hii[okk] = True
                        return True

            hii[okk] = False
            return False

        backtrack("", s)
        return len(result) > 0