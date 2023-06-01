S = input()
word = ["dream","dreamer","erase","eraser"]

while True:
    if len(S) == 0:
        print("YES")
        exit()
    flag = 1
    for i in word:
        if S.endswith(i):
            S = S[:-len(i)]
            flag = 0
            break
    if flag == 1:
        print("NO")
        exit()
    