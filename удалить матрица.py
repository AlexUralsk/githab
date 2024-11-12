n = int(input())
if n % 2 != 0:
    matrix = [[0] * n for _ in range(n)]
for i in matrix:
    print(*i)