def boring(lis):
    dicta = {num: lis.count(num) for num in lis}

    if len(set(lis)) == len(lis):
        return True

    values = list(dicta.values())
    if 1 in values:
        values.remove(1)
        if len(set(values)) == 1:
            return True
        elif len(set(values)) == 0:
            return True
        else:
            values.append(1)

    maximum = max(values)
    values[values.index(maximum)] -= 1

    if len(set(values)) == 1:
        return True
    elif len(set(values)) == 0:
        return True
    else:
        return False


def checker(inputok):
    inputok = inputok[::-1]
    gen1 = (inputok[i:] for i in range(0, len(inputok)))
    return gen1


input()
a = list(map(int, input().split()))
w = checker(a)
for i in w:
    if boring(i):
        print(len(i))

        break