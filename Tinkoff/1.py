a = list(map(int,input().split()))

if a==sorted(a) or a==sorted(a,reverse=True):
    print('YES')
else:
    print('NO')