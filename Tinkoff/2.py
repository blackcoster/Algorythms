n,m,k = a = list(map(int,input().split()))
ans1 = n*k
if ans1%m==0:
    ans = ans1//m
else:
    ans = ans1//m+1
print(ans)