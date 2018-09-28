"""
Given a array of numbers representing the stock prices of a company in chronological order,
write a function that calculates the maximum profit you could have made from buying and selling that stock once.
You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5,
since you could buy the stock at 5 dollars and sell it at 10 dollars.
"""

def compute(lis):
    profit = 0
    max_price = min_price = lis[0]
    for price in lis[1:]:
        if max_price < price:
            max_price = price
            if (max_price - min_price) > profit:
                profit = max_price - min_price
        elif min_price > price:
            min_price = max_price = price
    return(profit)

def main():
    l = map(int,(raw_input("Enter the stock prices? ")).split(' '))
    profit = compute(l)
    print(profit)

if __name__ == "__main__":
    main()