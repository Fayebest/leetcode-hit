class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for i in range(n)] for j in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i-1 >= 0 and j-1 >=0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                elif i-1 >= 0:
                    dp[i][j] = dp[i-1][j]
                elif j-1 >= 0:
                    dp[i][j] = dp[i][j-1]
        return dp[m-1][n-1]
            