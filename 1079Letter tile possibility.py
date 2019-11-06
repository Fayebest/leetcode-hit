class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        self.count=0
        self.backtrack(list(tiles),0)
        return self.count-1
        
    def backtrack(self, tiles,sta):
        self.count += 1
        for i in range(sta,len(tiles)):
            if i-sta >= 1 and  tiles[i] == tiles[i-1]:
                continue
            tiles[i],tiles[sta] = tiles[sta],tiles[i]
            self.backtrack(tiles,sta+1)
            tiles[i],tiles[sta] = tiles[sta],tiles[i]