word = list(input())
ans_word = word
contains_only_a = True
if len(word) <2:
    ans_word = []

else:
    if len(word)%2==0:
        for i in range(len(word)):
            if ord(word[i])>97:
                ans_word[i]='a'
                contains_only_a = False
                break
        if contains_only_a:
            ans_word[-1]='b'



    else:
        for i in range(len(word)):
            if ord(word[i]) > 97 and i!=len(word)//2:
                ans_word[i] = 'a'
                contains_only_a = False
                break
        if contains_only_a:
            ans_word[-1] = 'b'

print(''.join(ans_word))
