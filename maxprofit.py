def maxProfit(prices):
  buy = prices[0]
  profit = 0

  for i in prices[1:]:
    if buy > i:
      buy = i

    profit = max(profit, i - buy)

  return profit
