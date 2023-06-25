n = int(input())
s = list(map(int,input().split()))
sets = set(s)
dic = dict.fromkeys(sets,0)

max_vstr = 0
for num in s:
  if num in sets:
    dic[num] = dic[num]+1

for k,v in dic.items():
  # print(k,v)
  if v>max_vstr:
    max_vstr = v
    max = k
  
# print(dic)
print(max)
