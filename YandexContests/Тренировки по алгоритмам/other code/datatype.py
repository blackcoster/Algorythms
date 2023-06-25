x, y, year = map(int, input().split(' '))
r = range(1, 13)
if x==y:
    print(1)
elif x in r and y in r:
    print(0)
else:
    print(1)
