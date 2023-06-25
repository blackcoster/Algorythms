n,k = list(map(int,input().split()))
nums = list(map(int,input().split()))
sets = set(nums)
dic = {}
for num in sets:
    dic[num]=[] 

for i in range(len(nums)):
  cur_num = nums[i]
  dic[cur_num].append(i)


ans = 'NO'
# v = dic[key]
for key in dic:
  for i in range(len(dic[key])-1):#0..2
    
    if dic[key][i+1]-dic[key][i]<=k:

      
      ans = 'YES'

print(ans)