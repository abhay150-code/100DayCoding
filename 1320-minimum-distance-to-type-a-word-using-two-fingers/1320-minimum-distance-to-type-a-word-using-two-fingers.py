class Solution:
    def minimumDistance(self, word: str) -> int:
        n = len(word)
        memo = {}

        def dist(a, b):
            if a == -1 or b == -1:
                return 0
            ax, ay = divmod(a, 6)
            bx, by = divmod(b, 6)
            return abs(ax - bx) + abs(ay - by)

        def dp(i, f1, f2):
            if i == n:
                return 0
            
            key = (i, f1, f2)
            if key in memo:
                return memo[key]

            cur = ord(word[i]) - 65

            use_f1 = dist(f1, cur) + dp(i + 1, cur, f2)
            use_f2 = dist(f2, cur) + dp(i + 1, f1, cur)

            memo[key] = min(use_f1, use_f2)
            return memo[key]

        return dp(0, -1, -1)