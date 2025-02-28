class Solution:
    def shortestCommonSupersequence(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        dp = [[""]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                if s[i] == t[j]:
                    dp[i+1][j+1] = dp[i][j] + s[i]
                else:
                    dp[i+1][j+1] = dp[i+1][j] if len(dp[i+1][j]) > len(dp[i][j+1]) else dp[i][j+1]
        lcs = dp[m][n]
        i = j = 0
        res = []
        for c in lcs:
            while s[i] != c:
                res.append(s[i])
                i += 1
            while t[j] != c:
                res.append(t[j])
                j += 1
            res.append(c)
            i, j = i + 1, j + 1
        return "".join(res) + s[i:] + t[j:]
