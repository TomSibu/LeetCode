from typing import List

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_colors = {}
        color_counts = {}
        results = []
        
        for x, y in queries:
            if x in ball_colors:
                old_color = ball_colors[x]
                color_counts[old_color] -= 1
                if color_counts[old_color] == 0:
                    del color_counts[old_color]
            
            ball_colors[x] = y
            if y in color_counts:
                color_counts[y] += 1
            else:
                color_counts[y] = 1
            
            results.append(len(color_counts))
        
        return results
