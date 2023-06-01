#1行n数字
#a,b,c = map(int, input().split())
#num_list = list(map(int, input().split())) #リストバージョン

#n行n文字
#n = int(input())  # nは入力回数
#str_list = []
#for i in range(n):
#    str_list.append(list(input().split()))
#print(str_list)

#n行n数字
#n = int(input())  # nは入力回数
#num_list = []
#for i in range(n):
#    num_list.append(list(map(int,input().split())))
#print(num_list)

a = int(input())
b,c = map(int, input().split())
s = input()

print(a+b+c, s)