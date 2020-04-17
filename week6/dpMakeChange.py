#动态规划算法求解硬币找零问题
def dpMakeChange(coinValueList,change,minCoins,coinused):
    for cents in range(1,change + 1):
        coinCount = cents
        newCoin = 0 
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
                newCoin = j
        minCoins[cents] = coinCount
        coinused[cents] = newCoin
    return minCoins[change]

def printCoins(coinsUsed,change):
    coin = change
    while coin > 0:
        thisCoin = coinsUsed[coin]
        print(thisCoin)
        coin = coin - thisCoin

amnt = 63
clist = [1,5,10,21,25]
coinUsed = [0] * (amnt+1)
coinCount = [0] * (amnt+1)
print("Making change for", amnt, "requires")
print(dpMakeChange(clist, amnt, coinCount,coinUsed), "coins")
print("They are:")
printCoins(coinUsed, amnt)
print("The used list is as follows:")
print(coinUsed)
