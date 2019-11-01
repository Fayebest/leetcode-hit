class Solution:
    def numTilePossibilities(self, tiles):
        self.ans = []
        self.backtrack(list(tiles),0,[])
        return self.ans
        
    def backtrack(self,tiles,sta,path):
        self.ans.append(path[:])
        for i in range(sta,len(tiles)):
            if i-sta >= 1 and tiles[i] == tiles[i-1]:
                continue
            path += tiles[i]
            tiles[i],tiles[sta] = tiles[sta],tiles[i]
            self.backtrack(tiles,sta+1,path)
            tiles[i],tiles[sta] = tiles[sta],tiles[i]
            path.pop()