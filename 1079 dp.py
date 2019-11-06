class Solution:
    def numTilePossibilities(self, tiles) :
        alpha = []
        alphatemp = [0 for i in range(26)]
        dp = [[0 for i in range(8)] for j in range(8)]


        for i in tiles:
            alphatemp[ord(i) - ord('A')] += 1

        for i in alphatemp:
            if i != 0:
                alpha.append(i)


        for i in range(alpha[0]+1):
            dp[0][i] = 1

        count = alpha[0]
        for i in range(1, len(alpha)):
            count += alpha[i]
            for j in range(count+1):
                for k in range(0,min(j,alpha[i])+1):
                    dp[i][j] = dp[i][j] + dp[i-1][j-k]*int(self.c(j,k))

        ans = 0
        for i in range(8):
            ans += dp[len(alpha)-1][i]
        return ans-1


    def c(self,j,k):
        num = 1
        for i in range(1,j+1):
            num = num * i
        for i in range(1,j-k+1):
            num = num/i
        for i in range(1,k+1):
            num = num/i
        return num

a = Solution()
print(a.numTilePossibilities("CDC"))

