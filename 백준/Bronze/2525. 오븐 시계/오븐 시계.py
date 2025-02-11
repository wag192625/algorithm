h, m1 = map(int, input().split())
m2 = int(input())

m = m1 + m2
if m >= 60 :
  h = h + m // 60
  m = m % 60
  if h >=24 :
    h = h-24

print(h, m)