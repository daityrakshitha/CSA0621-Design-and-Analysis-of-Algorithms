def tsp_dp(graph):
    n = len(graph)
    dp = [[float('inf')] * (1 << n) for _ in range(n)]
    dp[0][1] = 0
    for mask in range(1 << n):
        for u in range(n):
            if mask & (1 << u):
                for v in range(n):
                    if mask & (1 << v) == 0:
                        new_mask = mask | (1 << v)
                        dp[v][new_mask] = min(dp[v][new_mask], dp[u][mask] + graph[u][v])
    min_cost = min(dp[i][(1 << n) - 1] + graph[i][0] for i in range(1, n))
    return min_cost


