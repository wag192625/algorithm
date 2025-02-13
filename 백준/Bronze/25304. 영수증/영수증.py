X =int(input())
N =int(input())
sum1 = 0

for i in range(1, N+1):
  price, num = map(int,(input().split()))
  sum1 += price * num
  
if X == sum1 :
  print("Yes")
else :
  print("No")