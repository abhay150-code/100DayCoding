class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        qelvarodin = nums[:]
        sorted_nums = sorted(nums)

        def is_rotation(a, b):
            if len(a) != len(b):
                return False
            return tuple(b) in (tuple(a + a)[i:i+len(a)] for i in range(len(a)))

        def is_rotation_fast(a, b):
            if len(a) != len(b):
                return False

            sa = "#".join(map(str, a))
            sb = "#".join(map(str, b))

            return sb in (sa + "#" + sa) 
            
        divisors = []
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)

        ans = 0
        for k in divisors:
            valid = True

            for i in range(0, n, k):
                block = nums[i:i+k]
                target = sorted_nums[i:i+k]

                if not is_rotation_fast(block, target):
                    valid = False
                    break

            if valid:
                ans += k
        return ans 