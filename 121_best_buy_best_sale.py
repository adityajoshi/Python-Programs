class BestBuy:
    def buyLowSellHigh(self, train):
        l, r = 0, 1
        maxP = 0

        while r < len(train):
            if train[l] < train[r]:
                profit = train[r] - train[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP


if __name__ == "__main__":
    b = BestBuy()
    train = [1, 3, 5, 7]
    maxP = b.buyLowSellHigh(train)
    print(maxP)
