N,M,K = map(int, input().split())
list = []
for i in range(N):
        row = []
        for j in range(M):
            row.append(j+i+1)
        list.append(row)

if list[N-1][M-1] <= K:
    print("YES")
    for row in list:
        for element in row:
            print(element, end=' ')
        print()
else:
    print("NO")