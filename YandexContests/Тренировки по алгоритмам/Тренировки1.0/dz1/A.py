have, want = list(map(int,input().split()))
type = input()
ans = have
if type =='freeze' and want< have:
  ans = want
elif type=='heat' and want>have:
  ans = want
elif type =='auto':
  ans = want
print(ans)