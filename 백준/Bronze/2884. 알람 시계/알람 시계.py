h, m = map(int, input().split())

m = m-45
if m<0 :
  m = 60+m
  h = h-1
  if h<0 :
    h= 24+h

print(h, m)