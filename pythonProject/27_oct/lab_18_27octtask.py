"""
1. Write a Python program to find the largest number in a list.

2. Write a Python program to find the smallest number in a list.

3. Write a Python program to sum all numbers in a list.

4. Write a Python program to multiply all numbers in a list.

5. Write a Python program to count the number of strings in a list where
 the string length is 2 or more and the first and last character are the same.
"""
l1=[1,2,89,7]
print("Maximum number in list" ,max(l1))
print("Minimum number in list ",min(l1))
sum=0
for x in l1:
    sum=sum+x
print("sum is ",sum )
mul=1
for x in l1:
    mul=mul*x
print("multiplication of all numbers in list",mul)
str=["aa","ffff","pramod","ashish","rupali"]
count=0
for i in str:
    if(len(i)>=2 and i[0]==i[-1]):
       count=count+1
print("String count",count)