n = input()
#R1G4G5B1B3
s = {}
for i in range(0,10):
    s[i]=[]

i = 1
while i<= len(n)-1:
    color = n[i-1]
    ring = int(n[i])
    # print(f'{ring}:{color}')
    s[ring].append(color)
    i+=2
# print(s)
sum = 0
for i in s:
   if 'R' in s[i] and 'G' in s[i] and 'B' in s[i]:
       sum+=1
print(sum)