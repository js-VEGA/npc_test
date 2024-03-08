import sys

N = int(input())

my_list = list(map(int, input().split()))  #문자열로 입력됨

result_list = []#결과 리스트에 값을 append하는 방식

if N != len(my_list):
    sys.exit()

for i in range(N):
    found = False  # 해당 원소를 찾았는지 여부 확인
    #while문은 시간 복잡도 높아서 대체
    for j in range(i + 1, N):
        if my_list[i] != my_list[j]:
            result_list.append(j + 1)
            found = True
            break
    if not found:
        result_list.append(-1)

result = ' '.join(map(str, result_list))
print(result)
