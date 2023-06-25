# n = int(input())
# h=[]
#
# for i in map(int,input().split()):
#     h.append(i)
# findot=h[0]
# sum=0
# finsum=abs((h[0]-h[-1])*n)
# for i in range(h[0],h[-1]+1):
#     for j in h:
#         dist = abs(i-j)
#     sum+=dist
#     print(f' до {i} сумма {sum}')
#     # if sum<finsum:
#     #     findot=i
#     #     finsum=sum
# # print(findot)


n= int(input())
s = input().split(' ')
sum=0
anssum = -1
# a = int(s[0])
# b = int(s[-1])
# ansdot=a

for i in s:
    i = int(i)
    for j in s:
        j=int(j)
        dist = abs(i-j)
        sum +=dist
    if sum<anssum or anssum==-1:
        ansdot=i
        anssum=sum
    sum=0
print(ansdot)

# if n%2==0:
#     print(s[n//2-1])
# else:
#     print(s[n//2])