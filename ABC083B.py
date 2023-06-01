N,A,B = map(int, input().split())

ans = 0

for i in range(1,N+1):
    degit = sum(list(map(int, str(i)))) 
    if degit >= A and degit <= B:
        ans += i

print(ans)