N,M,K = map(int, input().split())
list = []

if K>M+N-1:
    print("YES")
    for i in range(N):
        row = []
        for j in range(M):
            row.append(j+i+1)
        list.append(row)
    for row in matrix:
        for element in row:
            print(element, end=' ')
        print()
else:
    print("NO")