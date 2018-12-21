"""
Given an array of numbers representing the stock prices of a company in chronological order and an integer k, return the maximum profit you can make from k buys and sells.
You must buy the stock before you can sell it, and you must sell the stock before you can buy it again.

For example, given k = 2 and the array [5, 2, 4, 0, 1], you should return 3.
TODO: It is a dynamic problem, need to learn
"""

def main():
    stock_prices = map(int, raw_input("Enter the stock prices?\n").split())
    k = int(raw_input("No. of times you would buy?\n"))
    buys = [None] * k
    sells = [None] * k
    profits = [0] * k
    i = 0
    buys[i] = stock_prices[0]
    index = 1
    that_index = 1
    while(i < k and index < len(stock_prices)):
        if(sells[i] == None and (buys[i] == None or stock_prices[index] < buys[i])):
            buys[i] = stock_prices[index]
        elif(stock_prices[index] > buys[i]):
            profit = stock_prices[index] - buys[i]
            if profit > profits[i]:
                sells[i] = stock_prices[index]
                that_index = i
                profits[i] = profit

        index += 1
        if(index == len(stock_prices) - 1):
            i += 1
            index = that_index + 1

    print(buys)
    print(sells)
    print(profits)

if __name__ == '__main__':
    main()
