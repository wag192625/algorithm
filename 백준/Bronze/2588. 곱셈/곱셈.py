num1 = int(input())
num2 = int(input())

# 1의 자리 수 
print(num1 * (num2-int(num2/10)*10))
# 10의 자리 수 
print(num1 *int((num2-(int(num2/100)*100)-(num2-int(num2/10)*10))/10))
# 100의 자리 수 
print(num1 * int(num2/100))
# 전체 곱
print(num1 * num2)