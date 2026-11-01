def knapsack(w, p, c):
    n = len(w)
    dp = [[0] * (c + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, c + 1):
            if w[i - 1] <= j:
                dp[i][j] = max(p[i - 1] + dp[i - 1][j - w[i - 1]],
                               dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    print("Maximum Profit:", dp[n][c])

w = list(map(int, input("Enter weights: ").split()))
p = list(map(int, input("Enter profits: ").split()))
c = int(input("Enter capacity: "))

knapsack(w, p, c)