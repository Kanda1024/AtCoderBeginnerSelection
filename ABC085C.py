N,Y = map(int, input().split())

for i in range(int(Y/10000 + 1)):
    for j in range(int(Y/5000 + 1)):
        if N-i-j >= 0:
            if 10000 * i + 5000 * j + 1000 * (N - i - j) == Y:
                print(i, j, N-i-j)
                exit()

print("-1 -1 -1")