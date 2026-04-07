class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        end = nums[-1]

        while l < r:
            mid = (l+r) // 2
            if nums[mid] > end:
                l = mid + 1
            elif nums[mid] < end:
                r = mid
            
        return nums[l]