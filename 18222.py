k = int(input())
def toemos(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n%2:
        return 1-toemos(n//2)
    else:
        return toemos(n//2)
print(toemos(k-1))#수열은 0부터 시작하지만 우리는 1로 읽기 때문
