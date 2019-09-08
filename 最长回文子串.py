class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        dp =[[0 for i in range(len(s))] for i in range(len(s))]
        maxsta = 0
        maxend = 0
        for i in range(len(s)):
            for j in range(i-1,-1,-1):
                if s[j] == s[i] and (i-j<=2 or dp[i-1][j+1] == 1):
                    dp[i][j] = 1
                    if i-j > maxend - maxsta:
                        maxend = i
                        maxsta = j
        return s[maxsta:maxend+1]
                
                