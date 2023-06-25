n= int(input())
times_s = input().split()
times = []
min =  24*60
for time in times_s:
    times.append(int(time[:2])*60 + int(time[3:]))
times = sorted(times)

for i in range(n-1):
    if times[i+1]- times[i]<min:
        min = times[i+1]- times[i]

if times[0]+24*60 - times[-1] < min:
    min = times[0]+24*60 - times[-1]
print(min)