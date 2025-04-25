import sys
input = sys.stdin.readline

N, M = map(int, input().split())

matrix_A = [list(map(int,input().split())) for _ in range(N)]
matrix_B = [list(map(int,input().split())) for _ in range(N)]

answer = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        answer[i][j] = matrix_A[i][j] + matrix_B[i][j]
        print(answer[i][j], end=" ")
    print()