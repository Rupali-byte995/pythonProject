#Exception
a=int(input("Enter numberA"))
b=int(input("Enter number b"))
try:
    c=a/b
except Exception as error:
    print(error)

finally:
    print("I am executed always ")
