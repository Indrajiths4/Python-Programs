def count_arrays(N, K):
    MOD = 10000
    dp = [[0 for _ in range(N+1)] for _ in range(K+1)]
    for j in range(1, N+1):
        dp[1][j] = 1
    for i in range(2, K+1):
        for j in range(1, N+1):
            for k in range(1, j+1):
                if j % k == 0:
                    dp[i][j] = (dp[i][j] + dp[i-1][k]) % MOD
    return sum(dp[K]) % MOD
N = int(input())
K = int(input())
result = count_arrays(N, K)
print(result)