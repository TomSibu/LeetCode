class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def backtrack(tile_count):
            total = 0
            for tile in tile_count:
                if tile_count[tile] > 0:
                    tile_count[tile] -= 1
                    total += 1 + backtrack(tile_count)
                    tile_count[tile] += 1
            return total

        tile_count = Counter(tiles)
        return backtrack(tile_count)