kzz = int(input())
interactor = int(input())
checker = int(input())
itog = interactor
match interactor:
    case 0:
        if kzz!=0:
            itog = 3
        else:
            itog = checker
    case 1:
        itog = checker
    case 4:
        if kzz !=0:
            itog=3
        else:
            itog = 4
    case 6:
        itog = 0
    case 7:
        itog = 1
print(itog)
