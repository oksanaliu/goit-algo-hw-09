def find_coins_greedy(amount, coins):
    result = {}
    for coin in coins:
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount -= coin * count
    return result

def find_min_coins(amount, coins):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [-1] * (amount + 1)
    
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0 and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin
    
    if dp[amount] == float('inf'):
        return {}  # Немає способу розбити цю суму на монети
    
    # Відновлення кількості монет для заданої суми
    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin
    
    return result

# Використання функцій для прикладу
coins = [50, 25, 10, 5, 2, 1]
amount = 178

greedy_result = find_coins_greedy(amount, coins)
dp_result = find_min_coins(amount, coins)

print("Жадібний алгоритм:", greedy_result)
print("Динамічне програмування:", dp_result)