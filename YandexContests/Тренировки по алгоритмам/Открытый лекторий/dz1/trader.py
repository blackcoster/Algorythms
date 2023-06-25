n = int(input())
days = list(map(int, input().split()))
stek = [0]
sum = 0
has = 1000
min1 = 0
max1 = -1
min2 = -1
max2 = -1
for i in range(0, n):

    cur_day = days[i]
    if max1 == -1:
        if cur_day < days[min1]:
            min1 = i

        elif cur_day > days[min1]:
            max1 = i
    elif max1 != -1 and min2 == -1:
        if cur_day > days[max1]:
            max1 = i
        elif cur_day < days[min1]:
            min2 = i
    elif min2 != -1:
        if cur_day > days[min2]:
            max2 = i
            # print(f'max2/min2 - {days[max2] / days[min2]}')
            # print(f'max1/min1 - {days[max1] / days[min2]}')
            if days[max2] / days[min2] > days[max1] / days[min1]:
                min1, max1 = min2, max2
                min2,max2 = -1,-1

            else:
                max2 = -1
        elif cur_day < days[min2]:
            min2 = i
if max1 == -1:
    min1 = -1
print(min1 + 1, max1 + 1)
