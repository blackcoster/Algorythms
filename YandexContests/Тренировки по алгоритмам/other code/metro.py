n,i,j = map(int,input().split(' '))
oneway = abs(i-j)-1
oranother = n-2-oneway
print(min(oneway,oranother))
