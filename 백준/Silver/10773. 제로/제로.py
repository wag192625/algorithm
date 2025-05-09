import sys
input = sys.stdin.readline

K = int(input())

stack = []
for _ in range(K):
    input_num = int(input())
    if input_num == 0:
        stack.pop()
    else :
        stack.append(int(input_num))
    
print(sum(stack))