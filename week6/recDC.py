import time
#递归解法求解最少硬币问题
def recMc(coinValveList,change):
    minCoins = change
    if change in coinValveList:    #最小规模，直接返回
        return 1
    else:
        for i in [c for c in coinValveList if c <= change ]:
            numCoins = 1 + recMc(coinValveList, change-i)    #调用自身，减小规模
            if numCoins < minCoins:
                minCoins = numCoins
    return minCoins

#递归解法求解最少硬币问题，改进
def recDc(coinValveList,change,knowResults):
    minCoins = change
    if change in coinValveList:    #最小规模，直接返回
        knowResults[change] = 1
        return 1
    elif knowResults[change] >0:
        return knowResults[change]    
    else:
        for i in [c for c in coinValveList if c <= change ]:
            numCoins = 1 + recDc(coinValveList, \
                                 change-i,knowResults)    #调用自身，减小规模
            if numCoins < minCoins:
                minCoins = numCoins
                knowResults[change] = minCoins
    return minCoins

print(time.perf_counter())
print(recDc([1,5,10,25],63,[0]*64))
print(time.perf_counter())
