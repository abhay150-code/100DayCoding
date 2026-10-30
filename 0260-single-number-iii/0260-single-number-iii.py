class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        xor = 0
        for num in nums:
            xor ^= num
        
        lowbit = xor & -xor
        
        num1, num2 = 0, 0
        for num in nums:
            if num & lowbit:
                num1 ^= num
            else:
                num2 ^= num
                
        return [num1, num2]