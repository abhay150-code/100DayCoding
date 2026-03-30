class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        def solve(i, k, ok):
            if k == 0:
                ans.append(ok[:])
                return
            if i == n or k < 0:
                return

            ok.append(candidates[i])
            solve(i, k - candidates[i], ok)
            ok.pop()
            solve(i + 1, k, ok)
        solve(0, target, [])
        return ans