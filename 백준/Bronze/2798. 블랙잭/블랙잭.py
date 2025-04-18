import sys
input = sys.stdin.readline

N, M= map(int,input().split())
card_list = list(map(int, input().split()))

sum = 0

for i in range(N) :
    for j in range(i+1,N) :
        for k in range(j+1,N) :
            total = card_list[i] + card_list[j] + card_list[k]
            if total <= M :
                sum = max(sum,total)
                
print(sum)