import sys

N = int(input())
values = input()

list = values.split()#문자열로 입력됨

if N != len(list):
    sys.exit()

for i in range(N):
    j = i+1
    while j < N:
        if int(list[i]) != int(list[j]):
            list[i] = j+1 #인덱스 단위는 0부터 시작하므로
            break
        j += 1
    if j == N:
        list[i] = -1

    
result = ' '.join(map(str, list))
print(result)