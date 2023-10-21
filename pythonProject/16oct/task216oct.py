"""
Create a program that determines whether a given year is a leap year.
A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
Use an if-else statement to make this determination.
Input = 2024
Output = Leap year
"""
year = int(input("Enter year to check if it is leap year or not"))
if year % 4 == 0 or year%400 == 0 and year%100!=0:
    print("It is a leap year")
else:
    print("Not a leap year")
