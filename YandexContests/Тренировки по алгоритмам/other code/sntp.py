n = int(input())

days = list(map(int, input().split()))
money = 1000
max = 0
day = (-1, -1)

buy_index = 0
sell_index = -1
maybe_buy_index = -1

for i in range(1, n):
    price = days[i]
    if sell_index < 0:
        if price > days[buy_index]:
            sell_index = i
            dolya_buy = money / days[buy_index]
            max1 = days[sell_index] * dolya_buy - days[buy_index] * dolya_buy
            if max1 > max:
                max = max1
                day = (buy_index, sell_index)

        elif price < days[buy_index]:
            buy_index = i

    if sell_index > 0 and maybe_buy_index < 0:
        if price > days[sell_index]:
            sell_index = i
        elif price < days[buy_index]:
            maybe_buy_index = i

    if maybe_buy_index>0:
        if price < days[maybe_buy_index]:
            maybe_buy_index = i
        elif price > days[maybe_buy_index]:
            dolya_buy2 = money / days[maybe_buy_index]
            max1 = price * dolya_buy2 - days[maybe_buy_index] * dolya_buy2
            if max1 > max:
                max = max1
                day = (maybe_buy_index, i)
                buy_index,sell_index = maybe_buy_index,i
                maybe_buy_index =-1
            else:
                maybe_buy_index = -1
    # print(buy_index,sell_index,maybe_buy_index)

sell_index = sell_index if sell_index>0 else -1
buy_index = buy_index if sell_index>0 else -1
print(buy_index+1,sell_index+1)
