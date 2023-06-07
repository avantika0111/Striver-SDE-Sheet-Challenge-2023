import sys
def stockBuySell(stocks):
    mini = sys.maxsize
    profit = 0
    
    for i in range(len(stocks)):
        mini = min(mini, stocks[i])
        profit = max(profit, stocks[i] - mini)
    
    return profit

stocks = list(map(int, input().split()))
print(stockBuySell(stocks))