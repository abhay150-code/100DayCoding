class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        n = len(candidates)

        def backtrack(start, curr, summ):
            if summ > target:
                return

            if summ == target:
                res.append(curr[:])
                return


            for i in range(start, n):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                    
                curr.append(candidates[i])
                backtrack(i + 1, curr, summ + candidates[i])
                curr.pop()

        backtrack(0, [], 0)
        return res