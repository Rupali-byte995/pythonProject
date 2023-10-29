# Fibonacci
# 0 1 1 2 3 5 8 13
num = int(input("Enter number till which u want to create fibonacci series"))

a = 0
b = 1
i = 0
while i < num:
    print(a,end='\t')
    a, b = b, a + b
    i = i + 1
