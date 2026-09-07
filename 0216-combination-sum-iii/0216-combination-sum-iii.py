class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def backtrack(start, curr_sum, okk):
            if len(okk) == k:
                if curr_sum == n:
                    result.append(okk[:])
                return
            

            for i in range(start, 10):
                if curr_sum + i > n:
                    break
                
                okk.append(i)
                backtrack(i+1, curr_sum+i, okk)
                okk.pop()
            
        backtrack(1, 0, [])
        return result