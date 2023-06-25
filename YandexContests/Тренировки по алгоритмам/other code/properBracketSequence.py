def properTwelve(str):
    mas = []
    for i in str:
        if i=='(':
            mas.append(1)
        elif i==')':
            if mas==[]:
                return 'no'
            if mas.pop()==1:
                continue
    if mas==[]:
        return 'yes'
    else:
        return 'no'

def properThirteen(str):
    balance = 0
    for i in str:
        if i == '(':
            balance+=1

        if i == ')':
            balance-=1
        if balance < 0:
            return 0

    if balance == 0:
        return 1
    else:
        return 0
n = input()
print(properThirteen(n))
