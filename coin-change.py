def coin_change(coins, amount):
    dp = [999999] * (amount + 1)
    dp [0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i-coin]+1)
    print(dp)
    if dp[amount] == 999999:
        return "No solution found"
    return dp[amount]

coins = [1,5,6,8]
target = 4
ans = coin_change(coins, target)
print(ans)