import sys
input = sys.stdin.readline

# card_list의 카드를 3 장 뽑고, 그 합이 M과 가장 근사한 값
# N
# 1번째 줄
N, M = map(int,input().split()) 
# N = 10	# 딜러가 보여주는 숫자 카드의 개수
# M = 500	# 넘으면 안 되는 수
# 2번째 줄
card_list = list(map(int, input().split()))
# card_list = [93, 181, 245, 214, 315, 36, 185, 138, 216, 295]
sum = 0

# for i in card_list[::-1] :
#     card_list.pop()
#     for j in card_list[::-1] : 
#         card_list.pop()
#         for k in card_list[::-1] :
#             print('=======')
#             print('카드 리스트',card_list)
#             print('i = ', i)
#             print('j = ', j)
#             print('k = ', k)
#             sum += i+j+k		
#             if sum > M :
#                 card_list.pop()
#                 print('총 합', sum)
#                 sum = 0
#                 break
#             else :
#                 print('else',sum)
#                 break

for i in range(N) :
    for j in range(i+1,N) :
        for k in range(j+1,N) :
            total = card_list[i] + card_list[j] + card_list[k]
            if total <= M :
                sum = max(sum,total)
                
print(sum)