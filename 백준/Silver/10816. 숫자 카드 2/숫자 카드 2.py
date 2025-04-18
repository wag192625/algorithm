import sys
input = sys.stdin.readline

n = int(input())
list_n = list(map(int, input().split()))
m = int(input())
list_m = list(map(int, input().split()))
num_dict = {}

for i in list_n:
    if i in num_dict:
        num_dict[i] += 1
    else:
        num_dict[i] = 1

for value in list_m:
    counts = num_dict.get(value, 0)
    print(counts, end=" ")