N = int(input())
A =  list(map(int, input().split()))

ans = 100000000

for i in A:
    cnt = 0
    while True:
        if i%2 == 1:
            if cnt < ans:
                ans = cnt
            break
        else:
            i = i/2
            cnt += 1

print(ans)