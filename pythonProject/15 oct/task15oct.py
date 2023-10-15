"""Write a Python program to calculate the area of a circle given its radius using the formula
area=π×r^2 ( Take pie as 3.14
)
"""
r=int(input("Enter radius\n"))
area=3.14*r**2
print(f"area is {area}")
"""Create a program that takes two numbers as input 
and prints whether the first number is greater than, less than, or equal to the second number.
"""
a=int(input("Enter value of a"))
b=int(input("Enter value of b"))
print("a is greater than b",a>b)
print("a is less than b",a<b)
print("a is equal to b",a==b)
"""Use the ternary operator to find the maximum of three numbers entered by the user.
Develop a Python script that calculates the square and cube of a given number.
"""
a=int(input("Enter value of a"))
b=int(input("Enter value of b"))
c=int(input("Enter value of c"))
max_value=a if a>b else b
print(max_value if max_value>c else c)
print(a**2)