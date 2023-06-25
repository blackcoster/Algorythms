n = int(input())
i = 1
while True:
    if n-i>0:
        n=n-i

        if n>=i+1:
            i=i+1
            continue
        else:
            break

    else:
        break

print(i)