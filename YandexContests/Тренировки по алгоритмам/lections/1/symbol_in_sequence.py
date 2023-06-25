s = input()
dict = {}
been = set()
ans = 0
anssym = ''
for char in s:
    if char in been:
        dict[char]+=1
    else:
        been.add(char)
        dict[char] = 1
    if dict[char]>ans:
        ans = dict[char]
        anssym = char

print(anssym)