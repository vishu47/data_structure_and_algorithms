def maxProfit(prices: list[int]) -> int:
    mini = prices[0]
    maxi = 0

    for i in range(len(prices)):
        profit = prices[i] - mini
        maxi = max(profit, maxi)

        mini = min(mini, prices[i])

    return maxi


a = [7,6,4,3,1]
cc = maxProfit(a)
print(cc)
