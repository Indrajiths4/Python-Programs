def max_path_sum(grid):
    MOD = 10**9 + 7
    N = len(grid)
    dp = [[0, 0] for _ in range(N)]
    dp[0][0] = grid[0][0]
    dp[0][1] = grid[0][1]
    for i in range(1, N):
        for j in range(2):
            for k in range(2):
                if grid[i][j] > grid[i-1][k]:
                    dp[i][j] = max(dp[i][j], dp[i-1][k] + grid[i][j])
    return max(dp[-1]) % MOD
N = int(input())
grid = []
for _ in range(N):
    row = list(map(int, input().split()))
    grid.append(row)
result = max_path_sum(grid)
print(result)