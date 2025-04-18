import sys
input = sys.stdin.readline

N, M = map(int, input().split())
names={}
for _ in range(N + M) :
    name = input().rstrip()
    if name in names:
        names[name] += 1
    else:
        names[name] = 1
        
answer = []
for name, count in names.items():
    if count == 2 :
        answer.append(name)

answer.sort()

print(len(answer))
print(*answer, sep="\n")