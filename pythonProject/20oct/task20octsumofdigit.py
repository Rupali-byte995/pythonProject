#Program to find thesum of digits
num=int(input("Enter the number "))
sum=0
while num!=0 :
    digit=num%10
    sum=sum+digit
    num=int(num/10)
print(sum)