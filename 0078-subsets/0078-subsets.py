class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        arr = []

        def solve(i, ans):
            if i == len(nums):
                arr.append(ans[:])
                return

            ans.append(nums[i])
            solve(i + 1, ans)
            ans.pop()
            solve(i + 1, ans)

        solve(0, [])
        return arr