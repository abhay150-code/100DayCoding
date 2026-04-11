class Solution:
    def minimumDistance(self, nums):
        n = len(nums)
        
        pos = [[] for _ in range(n + 1)]
        
        for i in range(n):
            pos[nums[i]].append(i)

        ans = float('inf')

        for arr in pos:
            if len(arr) >= 3:
                for i in range(len(arr) - 2):
                    dist = 2 * (arr[i+2] - arr[i])
                    if dist < ans:
                        ans = dist

        return ans if ans != float('inf') else -1