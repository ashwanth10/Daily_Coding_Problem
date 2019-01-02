r"""
Find the minimum number of coins required to make n cents.

You can use standard American denominations, that is, 1sents, 5sents, 10sents, and 25sents.

For example, given n = 16, return 3 since we can make it with a 10sents, a 5sents, and a 1sents.
"""


def main():
    n = int(raw_input("Enter n?\n"))
    denominations = [ 1, 5, 10, 25]

    index = len(denominations) - 1
    coin_count = 0
    coins_required = []

    while(n):
        if  n >= denominations[index]:
            n -= denominations[index]
            coin_count += 1
            coins_required.append(denominations[index])
        else:
            index -= 1

    print("{}".format(coin_count))
    print("Coins required are {}".format(str(coins_required)))

if __name__ == '__main__':
    main()