with open("input.txt", "r") as file:
    str = file.read()

strconc = str.replace(' ','')
fin = strconc.replace('\n','')
dictut = dict()
for i in fin:
    dictut[i]=fin.count(i)


dictindexes = []
print(sorted(dictut))
for i in sorted(dictut):
    dictindexes.append(dictut[i])
zvezdochki=[]
for i in zvezdochki:
    zvezdochki.append(' ')

print(dictindexes)
for i in sorted(dictut.items(),key=lambda item:item[1],reverse=1):
    for j in dictut:
        if i==dictut[j]:
            # zvezdochki[st.index(i)]='*'
            print(dictindexes.index(i))
            # print(zvezdochki)

