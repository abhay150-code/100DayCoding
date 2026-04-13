from bisect import bisect_left, bisect_right

class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        n = len(robots)
        # Combine and sort robots to keep distance associations
        bot_data = sorted(zip(robots, distance))
        sorted_bots = [b[0] for b in bot_data]
        sorted_dist = [b[1] for b in bot_data]
        
        walls.sort()
        
        # Precompute wall counts in specific ranges using binary search
        def count_walls(start, end):
            if start > end: return 0
            l = bisect_left(walls, start)
            r = bisect_right(walls, end)
            return max(0, r - l)

        # dp[i][0] = max walls destroyed up to robot i, robot i NOT firing right
        # dp[i][1] = max walls destroyed up to robot i, robot i IS firing right
        dp = [[0, 0] for _ in range(n)]
        
        # Initialize for first robot
        # Left shot: blocked by nothing (endless line), but limited by distance
        left_range_0 = count_walls(sorted_bots[0] - sorted_dist[0], sorted_bots[0])
        dp[0][0] = left_range_0
        
        # Right shot: blocked by sorted_bots[1] if it exists
        limit_r0 = sorted_bots[1] - 1 if n > 1 else float('inf')
        right_range_0 = count_walls(sorted_bots[0], min(sorted_bots[0] + sorted_dist[0], limit_r0))
        dp[0][1] = right_range_0

        for i in range(1, n):
            curr_pos = sorted_bots[i]
            curr_dist = sorted_dist[i]
            prev_pos = sorted_bots[i-1]
            
            # --- Calculate possible wall gains for robot i ---
            # Walls between robot i-1 and robot i
            # Robot i firing Left
            fire_left_start = max(curr_pos - curr_dist, prev_pos + 1)
            walls_left = count_walls(fire_left_start, curr_pos)
            
            # Robot i firing Right
            limit_r = sorted_bots[i+1] - 1 if i + 1 < n else float('inf')
            fire_right_end = min(curr_pos + curr_dist, limit_r)
            walls_right = count_walls(curr_pos, fire_right_end)
            
            # Special case: Robot i-1 firing Right and Robot i firing Left 
            # cover overlapping walls. We must count the union of these walls.
            prev_dist = sorted_dist[i-1]
            fire_prev_right_end = min(prev_pos + prev_dist, curr_pos - 1)
            
            # Union of walls: walls in [prev_pos, prev_right_end] OR [curr_left_start, curr_pos]
            # Since walls are sorted, we find the min start and max end within the gap
            union_walls = count_walls(min(fire_prev_right_end, fire_left_start), curr_pos) if fire_left_start <= fire_prev_right_end else (walls_left + count_walls(prev_pos, fire_prev_right_end))

            # --- Update DP ---
            # To compute dp[i][0] (Robot i fires Left or nothing):
            # 1. i-1 fired Right: use union_walls (subtracting the single count already in dp[i-1][1])
            # Note: dp[i-1][1] already includes walls from robot i-1 firing right.
            # We add walls from i firing left that aren't already counted.
            
            # Option A: i-1 didn't fire right, i fires left
            option1 = dp[i-1][0] + walls_left
            # Option B: i-1 fired right, i fires left (handle overlap)
            # Walls in gap = count_walls(prev_pos, curr_pos)
            # We want to avoid double counting walls in (prev_pos, curr_pos)
            # if both bullets cover them.
            overlap_start = max(fire_left_start, prev_pos)
            overlap_end = min(fire_prev_right_end, curr_pos)
            overlap_count = count_walls(overlap_start, overlap_end)
            option2 = dp[i-1][1] + walls_left - overlap_count
            
            dp[i][0] = max(option1, option2, dp[i-1][0], dp[i-1][1]) # max includes not firing i at all
            
            # To compute dp[i][1] (Robot i fires Right):
            # This is simply the max of dp[i][0] (without the i-left shot) + walls_right
            # But wait, i firing right is independent of what i-1 did to the left.
            dp[i][1] = max(dp[i-1][0], dp[i-1][1]) + walls_right
            # Also consider robot i firing ONLY right (not left)
            # handled by the max() above.

        return max(dp[n-1][0], dp[n-1][1])