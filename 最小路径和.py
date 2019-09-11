class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid[0])
        n = len(grid)
        mar = [[0 for i in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                if i - 1 >= 0 and j - 1 >= 0:
                    mar[i][j] = min(mar[i-1][j], mar[i][j-1]) + grid[i][j]
                elif i - 1 >= 0:
                    mar[i][j] = mar[i-1][j] + grid[i][j]
                elif j - 1 >= 0:
                    mar[i][j] = mar[i][j-1] + grid[i][j]
        return mar[n - 1][m - 1]