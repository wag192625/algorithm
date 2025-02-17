import sys

s = int(input())

for _ in range(s) :
  n1, n2 = map(int, sys.stdin.readline().split())
  print(n1+n2)
