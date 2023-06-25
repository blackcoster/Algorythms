def properTwelve(str):
    mas = []
    for i in str:
        if i=='(':
            mas.append(i)
        if i=='{':
            mas.append(i)
        if i=='[':
            mas.append(i)

        if i==')' :
            if mas==[]:
                return 'no'
            if mas.pop()=='(':
                pass
            else:
                return 'no'
        if i == '}':
            if mas == []:
                return 'no'
            if mas.pop() == '{':
                pass
            else:
                return 'no'
        if i == ']':
            if mas == []:
                return 'no'
            if mas.pop() == '[':
                pass
            else:
                return 'no'

    if mas==[]:
        return 'yes'
    else:
        return 'no'

str = input()
print(properTwelve(str))