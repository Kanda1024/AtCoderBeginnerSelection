N = int(input())

t = 0
x = 0
y = 0

for i in range(N):
    t_,x_,y_ = map(int, input().split())
    d = abs(x_ - x) + abs(y_ - y)
    if not(((t_-t)-d)%2 == 0 and (t_-t)-d >= 0):
        print("No")
        exit()
    t = t_
    x = x_
    y = y_

print("Yes")