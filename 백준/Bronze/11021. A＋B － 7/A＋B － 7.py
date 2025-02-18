import sys

s = int(input())

for i in range(s) :
  n1, n2 = map(int,input().split())
  print('Case #'+str(i+1)+':',n1+n2)
